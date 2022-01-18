from pathlib import Path
import re, sys

p = Path(input('directory: '))
if not p.exists():
    print(f'invalid path: {p}')
    sys.exit()
r = re.compile(fr'{input("regex: ")}')


print(f'searching for {r.pattern} in {p}')
for text_file in p.glob('*.txt'):
    print(f'looking in {text_file}')
    with open(text_file, 'r') as f:
        hits = r.finditer(f.read())
        for h in hits:
            print(f'found {h.group()} at {h.span()}')