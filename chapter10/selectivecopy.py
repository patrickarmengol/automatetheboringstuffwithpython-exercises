# walks through directory tree and searches for files with a cetain extension, copies files to a new folder

from pathlib import Path
import shutil

def main():
    input_dir = Path(input('input dir to search in: '))
    output_dir = Path(input('input dir to copy files to: '))
    output_dir.mkdir(parents=True, exist_ok=True)
    extension = input('input extention: ')
    # looks like the glob updates as new files are added so i tupled it; a better way to do this would be to exclude the output directory from the glob
    files_with_ext = tuple(input_dir.rglob(f'*{extension if "." in extension else "."+extension}'))
    for f in files_with_ext:
        shutil.copy(f, output_dir / f.name)
    


if __name__ == '__main__':
    main()