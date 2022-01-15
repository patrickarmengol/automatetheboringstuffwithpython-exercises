#! python3
# bulletpointadder.py - adds wiki bullet points to the start of each line of text on the clipboard

"""
Lists of animals
Lists of aquarium life
Lists of biologists by author abbreviation
Lists of cultivars
"""

"""
* Lists of animals
* Lists of aquarium life
* Lists of biologists by author abbreviation
* Lists of cultivars
"""


import pyperclip

text = pyperclip.paste()

lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

newtext = '\n'.join(lines)
pyperclip.copy(newtext)