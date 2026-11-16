"""Cross-platform coordinator build. Fails in place; does not move or hide invalid files."""
import pathlib
import subprocess
import sys
from release_policy import approved

ROOT = pathlib.Path(__file__).resolve().parents[1]


def run(command):
    subprocess.run(command, cwd=ROOT, check=True)


if __name__ == '__main__':
    files = sorted((ROOT / 'research/metro/transcribed').glob('*.json')) + sorted((ROOT / 'research/yilan/transcribed').glob('*.json'))
    files = [p for p in files if approved(ROOT,p)]
    run([sys.executable, 'scripts/check_transcript.py', *(f.relative_to(ROOT).as_posix() for f in files)])
    run([sys.executable, 'scripts/prepare_data.py'])
    run([sys.executable, 'scripts/subset_font.py'])
    # Node is cross-platform; shell-free invocation also works on Windows npm.cmd.
    run(['node', '--test', *map(str, sorted((ROOT / 'tests').glob('*.test.mjs')))])
    run(['node', 'scripts/build.mjs'])
    print('Build complete; nothing was published. Follow handoff/REVIEW_POLICY.md for the current user-approved review scope and deployment steps.')
