# guess the number game

import random

secret_num = random.randint(1,20)
print('I am thinking of a number between 1 and 20')

# ask player to guess 6 times
for guesses_taken in range(1, 7):
    print('take a guess')
    guess = int(input())

    if guess < secret_num:
        print('your guess is too low')
    elif guess > secret_num:
        print('your guess is too high')
    else:
        break

if guess == secret_num:
    print('good job. you guessed the number in ' + str(guesses_taken) + ' guesses')
else:
    print('you\'re bad at this game. the number was ' + str(secret_num))