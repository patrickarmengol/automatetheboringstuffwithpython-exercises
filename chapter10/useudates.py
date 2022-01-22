#! python3
# useudates.py - rename filenames with american MM-DD-YYYY formate to european DD-MM-YYYY
# book example specifies above formats with capital letters which means number of digits matter, but the regex pattern ends up doing mm-dd-YYYY
# also, the code seems overcomplicated. just use re.sub instead...
# also also, i this kind of script would never be needed if we all just used ISO 8601 standard

import shutil, os, re, sys

input_dir = input('input dir for date conversion: ')
if not os.path.exists(input_dir):
    print(f'path {input_dir} does not exists')
    sys.exit()
abs_dir = os.path.abspath(input_dir)

for us_filename in os.listdir(abs_dir):
    eu_filename = re.sub(r'([01]\d)-([0-3]\d)-((19|20)\d\d)', r'\2-\1-\3', us_filename)
    us_filepath = os.path.join(abs_dir, us_filename)
    eu_filepath = os.path.join(abs_dir, eu_filename)
    print(f'renaming "{us_filename}" to "{eu_filename}"')
    #shutil.move(us_filepath, eu_filepath)
