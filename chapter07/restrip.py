import re


def restrip(unstripped, chars=' '):
    # i'm just going to assume any special characters passed in chars are escaped
    return re.compile(fr'^[{chars}]*|[{chars}]*$').sub('',unstripped)

test1 = '  as d f    '
test2 = '-_-_-qw--_-__-_er---__-'

print(f'{test1}\n{restrip(test1)}')
print(f'{test2}\n{restrip(test2, "-_")}')

