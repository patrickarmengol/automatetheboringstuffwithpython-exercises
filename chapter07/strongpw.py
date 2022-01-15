import re

eight_plus_chars = re.compile(r'.{8,}')
both_cases = re.compile(r'[a-z].*[A-Z]|[A-Z].*[a-z]')
digit = re.compile(r'\d')

def is_strong_pw(pw):
    if eight_plus_chars.search(pw) and both_cases.search(pw) and digit.search(pw):
        return True
    else:
        return False

test_pws = ['password', 'hunter2', '123Abc', 'qweR2zxcvs']

for test in test_pws:
    print(f'password: {test}  result: {"passed" if is_strong_pw(test) else "failed"}')