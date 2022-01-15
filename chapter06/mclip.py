#! python3
# mclip.py - a multi-clipboard program

import sys, pyperclip

TEXT = {
    'agree': """ok, sounds good""",
    'busy': """sorry, I'm busy""",
    'upsell': """that's it? give me more"""
}

if len(sys.argv) < 2:
    print('usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1] # first command line arg

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('text for ' + keyphrase + ' copied to clipboard')
else:
    print('there is no text for ' + keyphrase)
