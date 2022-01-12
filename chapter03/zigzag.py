# zigzag pattern printer
# trying without looking at book example

import sys, time

indent = 0
direction = 1
try:
    while True:
        time.sleep(0.1)
        print(' ' * indent + '********')
        indent += direction
        if indent == 10 or indent == 0:
            direction = -direction
except KeyboardInterrupt:
    sys.exit()