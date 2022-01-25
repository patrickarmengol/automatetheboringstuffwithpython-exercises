#! python3
# mapit.py - launches a map in the browser using an address from the command line or clipboard
# example: python mapit.py "870 Valencia St, San Francisco, CA 94110"
# gmaps url format: https://www.google.com/maps/place/<address>
# this script is pretty useless and I find it kind of funny that the author made a comparison table to outline its advantages
# in reality it's much more cumbersome to run the script
# ddg has a !gmaps bang that's pretty convenient

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    address = sys.argv[1]
else:
    address = pyperclip.paste()

webbrowser.open(f'https://www.google.com/maps/place/{address}')