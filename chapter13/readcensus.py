#! python3
# readcensus.py - tabulates pop and number of census tracts for each county

import openpyxl, pprint

print('opening workbook...')

wb = openpyxl.load_workbook('chapter13/censuspopdata.xlsx')
sheet = wb['Population by Census Tract']

county_data = {}

print('reading rows...')

for row in range(2, sheet.max_row + 1):
    state = sheet[f'B{row}'].value
    county = sheet[f'C{row}'].value
    pop = sheet[f'D{row}'].value

    county_data.setdefault(state, {})
    county_data[state].setdefault(county, {'tracts': 0, 'pop': 0})

    county_data[state][county]['tracts'] += 1
    county_data[state][county]['pop'] += int(pop)

print('writing results...')

with open('chapter13/census2010.py', 'w') as result_file:
    result_file.write('all_data = ' + pprint.pformat(county_data))

print('done')