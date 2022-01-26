# sample commandline:
# python blankrowinserter.py 3 2 my_produce.xlsx

import openpyxl, sys

def insert_blanks(row_index, num_rows, file_to_mod):
    wb = openpyxl.load_workbook(file_to_mod)
    sheet = wb.active

    sheet.insert_rows(idx=row_index, amount=num_rows) # i assume this didn't exist when the book was written?

    wb.save(file_to_mod)

def main():
    if len(sys.argv) < 4:
        print('usage: python blankrowinserter.py <row_index> <num_rows> <file_to_mod>')
    else:
        insert_blanks(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3])



if __name__ == '__main__':
    main()