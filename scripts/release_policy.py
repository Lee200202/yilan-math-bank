"""Only approved transcript bytes can enter a public build; drafts stay on disk."""
import hashlib
import json
import pathlib


def approved(root, path):
    root, path = pathlib.Path(root), pathlib.Path(path)
    policy = root / 'research/release-transcripts.json'
    if not policy.exists():
        raise ValueError('Missing verified transcript release policy')
    records = json.loads(policy.read_text(encoding='utf-8'))['papers']
    entry = records.get(path.stem)
    if not entry:
        return False
    actual = hashlib.sha256(path.read_bytes().replace(b'\r\n', b'\n')).hexdigest()
    if actual != entry['transcriptSha256']:
        raise ValueError(f'Approved transcript changed after review: {path.stem}')
    return True
