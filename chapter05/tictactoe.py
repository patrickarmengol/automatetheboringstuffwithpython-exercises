



the_board = {
    'top-l': ' ', 'top-m': ' ', 'top-r': ' ',
    'mid-l': ' ', 'mid-m': ' ', 'mid-r': ' ',
    'bot-l': ' ', 'bot-m': ' ', 'bot-r': ' '
}

def print_board(board):
    print(board['top-l'] + '|' + board['top-m'] + '|' + board['top-r'])
    print('-+-+-')
    print(board['mid-l'] + '|' + board['mid-m'] + '|' + board['mid-r'])
    print('-+-+-')
    print(board['bot-l'] + '|' + board['bot-m'] + '|' + board['bot-r'])


turn = 'X'

for i in range(9):
    print_board(the_board)
    print('turn for ' + turn + '. move on which space?')
    move = input()
    the_board[move] = turn
    turn = 'X' if turn == 'O' else 'O'
print_board(the_board)