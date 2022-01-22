#! python3
# backuptozip.py - copies an entire folder and its contents into a zip file whose filename increments

import zipfile, os

def backuptozip(directory):
    directory = os.path.abspath(directory)
    number = 1
    while True:
        zip_filename = os.path.basename(directory) + '_' + str(number) + '.zip'
        if not os.path.exists(zip_filename):
            break
        number = number + 1
    
    print(f'creating {zip_filename}')
    backup_zip = zipfile.ZipFile(zip_filename, 'w')
    
    for dirname, subdirs, filenames in os.walk(directory):
        print(f'adding files in {dirname}')
        backup_zip.write(dirname)
        for filename in filenames:
            if filename.startswith(os.path.basename(directory) + '_'):
                continue
            backup_zip.write(os.path.join(dirname, filename))
    backup_zip.close()

    print('done')

backuptozip(input('input directory for backup: '))