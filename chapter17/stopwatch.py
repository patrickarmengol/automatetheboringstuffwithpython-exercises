import time, sys

print('press ENTER to begin; aftwerards, press ENTER to lap; press Ctrl+C to quit')
input()
print('started')

start_time = time.time()
last_time = start_time
lap_num = 1

try:
    while True:
        input()
        step = time.time()
        lap_time = round(step - last_time, 2)
        total_time = round(step - start_time, 2)
        print(f'lap #{lap_num}: {total_time} ({lap_time})', end='')
        lap_num += 1
        last_time = step
except KeyboardInterrupt:
    print('\ndone')