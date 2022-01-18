# i really don't like how i did this but whatever
# i remember having an easier time with jinja templates

import re

placeholder_regex = re.compile('ADJECTIVE|NOUN|VERB')
text = ''

with open('chapter09/madtext.txt', 'r') as f:
    text = f.read()
    while True:
        placeholder = placeholder_regex.search(text)
        if placeholder == None:
            break
        ps = placeholder.group().lower()
        print(f'enter {"an" if ps[0] == "a" else "a"} {ps}')
        replacement = input()
        text = placeholder_regex.sub(replacement, text, 1)
    print(text)

with open('chapter09/madfilled.txt', 'w') as f:
    f.write(text)
