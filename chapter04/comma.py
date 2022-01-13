

def commafy(items):
    return ' and '.join(items) if len(items) <= 2 else f"{', '.join(items[:-1])}, and {items[-1]}"

asdf = ['a', 's', 'd', 'f']
print(commafy(asdf))

qwer = ['q', 'w']
print(commafy(qwer))

zxcv = ['z']
print(commafy(zxcv))

o = []
print(commafy(o))