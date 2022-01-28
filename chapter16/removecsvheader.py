import csv, os

os.makedirs('header_removed', exist_ok=True)

for csv_fn in os.listdir('.'):
    if not csv_fn.endswith('.csv'):
        continue
    print(f'removing header from {csv_fn}')

    with open(csv_fn, 'r') as csv_in, open(f'header_removed/{csv_fn}', 'w', newline='') as csv_out:
        csv_reader = csv.reader(csv_in)
        csv_writer = csv.writer(csv_out)
        for row in csv_reader:
            if csv_reader.line_num == 1: # no header detection; just assumes header exists for all files
                continue
            csv_writer.writerow(row)

        