import random

guess = ''
while guess not in ('heads', 'tails'):
    print('guess the coin toss! enter heads or tails:')
    guess = input()
toss = random.randint(0,1)
if toss == guess: # int vs string
    print('you got it!')
else:
    print('nope! guess again!')
    guesss = input() # sss, also no input val
    if toss == guess:
        print('you got it!')
    else:
        print('nope. you bad.')