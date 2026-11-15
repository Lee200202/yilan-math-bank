"""Restore one target's ignored original on another machine, checking its pinned SHA256.

Usage: python scripts/fetch_paper.py PAPER_ID
Does not crawl, alter metadata, or extract archive paths into the filesystem.
"""
import hashlib
import io
import json
import pathlib
import re
import urllib.parse
import urllib.request
import zipfile

ROOT = pathlib.Path(__file__).resolve().parents[1]


def checked(data, expected):
    if not expected or hashlib.sha256(data).hexdigest() != expected:
        raise ValueError('Original checksum changed; keep the old evidence and re-review the source')
    return data


def download(url):
    parsed = urllib.parse.urlsplit(url)
    if parsed.scheme != 'https':
        raise ValueError('Only public HTTPS originals are supported')
    fid = re.search(r'/file/d/([^/]+)', parsed.path)
    if parsed.hostname == 'drive.google.com' and fid:
        params = {'export': 'download', 'id': fid.group(1)}
        params.update({k: v[0] for k, v in urllib.parse.parse_qs(parsed.query).items() if k.lower() == 'resourcekey'})
        url = 'https://drive.usercontent.google.com/download?' + urllib.parse.urlencode(params)
    else:
        url = urllib.parse.urlunsplit(parsed._replace(fragment=''))
    # Official filenames often contain literal Chinese; preserve existing % escapes.
    url = urllib.parse.quote(url, safe=":/?=&%,#()")
    request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (public-exam-handoff/1.0)'})
    with urllib.request.urlopen(request, timeout=60) as response:
        return response.read()


def member_name(info):
    if info.flag_bits & 0x800:
        return info.filename
    for encoding in ('big5', 'utf-8'):
        try:
            return info.filename.encode('cp437').decode(encoding)
        except (UnicodeEncodeError, UnicodeDecodeError):
            pass
    return info.filename


def fetch(pid):
    targets = [t for p in (ROOT / 'research/targets').glob('*.json')
               for t in json.loads(p.read_text(encoding='utf-8')) if isinstance(t, dict) and t.get('paperId') == pid]
    if not targets:
        raise ValueError('Paper is not in the reviewed target lists')
    target = targets[0]
    destination = (ROOT / target['pdf']).resolve()
    if not destination.is_relative_to(ROOT):
        raise ValueError('Target path escapes repository')
    paper = next(p for p in json.loads((ROOT / 'public/data/papers.json').read_text(encoding='utf-8')) if p['id'] == pid)
    if destination.exists():
        checked(destination.read_bytes(), paper['sha256'])
        return destination
    inventory = json.loads((ROOT / 'research/metro/metro-inventory.json').read_text(encoding='utf-8'))
    rows = {f['id']: f for s in inventory['sources'].values() for f in s['files'] if 'id' in f}
    row = rows.get(pid, paper)
    if row.get('archiveId'):
        parent = rows[row['archiveId']]
        data = checked(download(parent['sourceUrl']), parent['sha256'])
        if not zipfile.is_zipfile(io.BytesIO(data)):
            raise ValueError('This archive needs its recorded 7z/rar extractor; no guessed member extraction')
        with zipfile.ZipFile(io.BytesIO(data)) as archive:
            matches = [entry for entry in archive.infolist() if row['archiveMember'] in (entry.filename, member_name(entry))]
            if len(matches) != 1:
                raise ValueError('Archive member is ambiguous or changed')
            data = archive.read(matches[0])
    else:
        data = download(paper['sourceUrl'])
    checked(data, paper['sha256'])
    if destination.suffix.lower() == '.pdf' and not data.startswith(b'%PDF'):
        raise ValueError('Server returned a non-PDF response; do not transcribe a login or error page')
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(data)
    return destination


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('paper_id')
    args = parser.parse_args()
    print(fetch(args.paper_id).relative_to(ROOT))
