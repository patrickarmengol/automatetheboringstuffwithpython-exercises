# find beeeg files

from pathlib import Path
import os

def main():
    input_dir = Path(input('input directory to search for big files: '))
    for dirname, subdirs, files in os.walk(input_dir):
        for f in files:
            if os.path.getsize(Path(dirname)/f) > 100000000:
                print(f'deleting {Path(dirname)/f}')

if __name__ == '__main__':
    main()