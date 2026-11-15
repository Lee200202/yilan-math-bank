"""Cross-platform coordinator build. Fails in place; does not move or hide invalid files."""
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]


def run(command):
    subprocess.run(command, cwd=ROOT, check=True)


if __name__ == '__main__':
    files = sorted((ROOT / 'research/metro/transcribed').glob('*.json')) + sorted((ROOT / 'research/yilan/transcribed').glob('*.json'))
    run([sys.executable, 'scripts/check_transcript.py', *map(str, files)])
    run([sys.executable, 'scripts/prepare_data.py'])
    run([sys.executable, 'scripts/subset_font.py'])
    # Node is cross-platform; shell-free invocation also works on Windows npm.cmd.
    run(['node', '--test', *map(str, sorted((ROOT / 'tests').glob('*.test.mjs')))])
    run(['node', 'scripts/build.mjs'])
    print('Build complete. PDF, every-page visual review and live acceptance are still required; nothing was published.')
