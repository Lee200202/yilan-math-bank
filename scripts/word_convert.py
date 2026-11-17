"""Unattended Word -> .docx conversion with a hard timeout (for legacy .doc papers).

Usage: python -X utf8 scripts/word_convert.py <input.doc> <output.docx> [timeout_seconds]

Runs scripts/word_convert_one.ps1 in a child PowerShell. It only ever touches the Word process that THIS run started
(a Word that was already running, e.g. the user's own document, is never closed). On timeout it reports the last logged
step, so a hidden dialog can be diagnosed, then stops only the child process tree it created.
"""
import os
import pathlib
import subprocess
import sys
import tempfile
import time

ROOT = pathlib.Path(__file__).resolve().parents[1]


def word_pids():
    raw = subprocess.run(['tasklist', '/FI', 'IMAGENAME eq WINWORD.EXE', '/FO', 'CSV', '/NH'], capture_output=True).stdout or b''
    out = raw.decode('utf-8', errors='replace')
    return {int(line.split('","')[1]) for line in out.splitlines() if line.startswith('"WINWORD.EXE"')}


def convert(src, dst, timeout=90):
    src, dst = pathlib.Path(src).resolve(), pathlib.Path(dst).resolve()
    log = pathlib.Path(tempfile.gettempdir()) / ('wordconv_' + src.stem[:40] + '.log')
    before = word_pids()
    cmd = ['powershell', '-NoProfile', '-NonInteractive', '-ExecutionPolicy', 'Bypass', '-File', str(ROOT / 'scripts/word_convert_one.ps1'),
           '-InputPath', str(src), '-OutputPath', str(dst), '-LogPath', str(log)]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8', errors='replace')
    t0 = time.time()
    while p.poll() is None and time.time() - t0 < timeout:
        time.sleep(0.5)
    last = log.read_text(encoding='utf-8', errors='replace').strip().splitlines()[-1:] if log.exists() else ['(no log)']
    if p.poll() is None:
        mine = word_pids() - before
        subprocess.run(['taskkill', '/T', '/F', '/PID', str(p.pid)], capture_output=True)
        for pid in mine:  # only Word processes started by this run
            subprocess.run(['taskkill', '/F', '/PID', str(pid)], capture_output=True)
        return False, 'TIMEOUT after %ds; last step: %s' % (timeout, last[0])
    ok = p.returncode == 0 and dst.exists() and dst.stat().st_size > 0
    return ok, last[0]


if __name__ == '__main__':
    ok, msg = convert(sys.argv[1], sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 90)
    print(('OK ' if ok else 'FAIL ') + msg)
    sys.exit(0 if ok else 1)
