import random

num_streaks = 0

for experiment_number in range(10000):
    # flip 100 times
    flips = [random.randint(0,1) for i in range(100)]
    for flip in range(len(flips) - 6):
        if flips[flip:flip+6] in ([1,1,1,1,1,1], [0,0,0,0,0,0]):
            num_streaks += 1
            break

print(f'{num_streaks/100}% chance of streak')
        