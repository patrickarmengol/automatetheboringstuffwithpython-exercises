# filling gaps in file numbering
# i'm thinking maybe i just count files, sort by filename, then use shutil.move
# or maybe just glob and enumerate and rename

from pathlib import Path
import re, os


def main():
    input_dir = Path(input('input directory to search for gaps: '))
    for i, f in enumerate(sorted(input_dir.glob('asdf*.txt')), start=1):
        f.rename(f.parent / f'asdf{i:03}.txt')

if __name__ == '__main__':
    main()