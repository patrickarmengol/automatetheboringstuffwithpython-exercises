#! python3
# mcb.pyw - saves and loads pieces of text to the clipboard
# usage: python mcb.pyw save <keyword> - saves clipboard to keyword
#        python mcb.pyw <keyword> - loads specified text to clipboard
#        python mcb.pyw list - loads all keywords to clipboard

import shelve, pyperclip, sys # eww using sys.argv to handle commandline args

mcb_shelf = shelf.open('mcb')

if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcb_shelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete':
        if sys.argv[2].lower() == 'all':
            for key in mcb_shelf.keys():
                del mcb_shelf[key]
        elif sys.argv[2].lower() in mcb_shelf.keys():
            del mcb_shelf[sys.argv[2].lower()]
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])

mcb_shelf.close()

