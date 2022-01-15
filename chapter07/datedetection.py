import re

DDMMYYYY_format = re.compile(r'''
    (0[1-9]|[1-2][0-9]|3[0-1])
    /
    (0[1-9]|1[0-2])
    /
    ([1-2][0-9][0-9][0-9])
''', re.VERBOSE)

test_text = 'valid: 22/12/1414, invalid day: 32/12/1414, invalid month: 01/14/1414, invalid year: 01/01/3000, valid leap: 29/02/2000, invalid leap: 29/02/2001'


def find_dates(text):
    found_dates = DDMMYYYY_format.findall(text)
    valid_dates = []
    for d in found_dates:
        if check_valid_date(d):
            valid_dates.append('/'.join(d))
    return valid_dates


def check_valid_date(date):
    day = date[0]
    month = date[1]
    year = date[2]
    if month in ['04','06','09','11'] and day <= '30':
        return True
    elif month in ['01','03','05','07','08','10','12'] and day <= '31':
        return True
    elif month == '02':
        if int(year) % 4 == 0 and day == '29':
            return True
        elif day == '28':
            return True
    return False

print(f'test text - \'{test_text}\'')
print(find_dates(test_text))
