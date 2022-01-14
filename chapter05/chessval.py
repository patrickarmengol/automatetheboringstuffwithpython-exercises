valid_board = {'H1': 'bK', 'C6': 'wQ', 'G2': 'bB', 'H5': 'bQ', 'E3': 'wK'}
invalid_king_board = {'H1': 'bK', 'H2': 'bK', 'C6': 'wQ', 'G2': 'bB', 'H5': 'bQ', 'E3': 'wK'}
invalid_space_board = {'T1': 'bK', 'C6': 'wQ', 'G2': 'bB', 'H5': 'bQ', 'E3': 'wK'}
invalid_pawns_board = {'A1': 'bK', 'H1': 'wK', 'C1': 'bP', 'C2': 'bP', 'C3': 'bP', 'C4': 'bP', 'C5': 'bP', 'C6': 'bP', 'C7': 'bP', 'C8': 'bP', 'D1': 'bP'}


def is_valid_chess_board(board):
    # 1 black king, 1 white king, at most 16 per color, at most 8 pawns per color, pieces on valid space

    # check for 1 of each king
    if list(board.values()).count('bK') != 1 or list(board.values()).count('wK') != 1:
        return False
    
    # count pieces and pawns per color
    piece_count = {'w': 0, 'b': 0}
    pawn_count = {'w': 0, 'b': 0}
    for piece in board.values():
        piece_count[piece[0]] += 1
        if piece[1] == 'P':
            pawn_count[piece[0]] += 1
    if piece_count['w'] > 16 or piece_count['b'] > 16 or pawn_count['w'] > 8 or pawn_count['b'] > 8:
        return False

    # check valid space
    for space in board.keys():
        if space[0] not in 'ABCDEFGH' or space[1] not in '12345678':
            return False

    return True

print(str(is_valid_chess_board(valid_board)))
print(str(is_valid_chess_board(invalid_king_board)))
print(str(is_valid_chess_board(invalid_space_board)))
print(str(is_valid_chess_board(invalid_pawns_board)))