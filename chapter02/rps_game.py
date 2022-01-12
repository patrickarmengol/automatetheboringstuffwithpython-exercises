# rock paper scissors game

import random, sys

print('rock, paper, scissors')

wins = 0
losses = 0
ties = 0

while True:
    
    print(f'{wins} wins, {losses} losses, {ties} ties')
    
    # get player choice
    while True:
        print('enter your move: (r)ock, (p)aper, (s)cissors, or (q)uit')
        player_move = input()
        if player_move == 'q':
            sys.exit()
        elif player_move in 'rps':
            break
        else:
            print('type r, p, s, or q')
    
    # display player choice
    if player_move == 'r':
        print('rock vs...')
    elif player_move == 'p':
        print('paper vs...')
    elif player_move == 's':
        print('scissors vs...')
    
    # get and display computer choice
    computer_move = random.choice('rps')
    if computer_move == 'r':
        print('rock')
    elif computer_move == 'p':
        print('paper')
    elif computer_move == 's':
        print('scissor')
    
    # who wins?
    if player_move == computer_move:
        print('it\'s a tie')
        ties += 1
    elif player_move + computer_move in ('rs', 'pr', 'sp'):
        print('you win')
        wins += 1
    else:
        print('you lose')
        losses += 1


