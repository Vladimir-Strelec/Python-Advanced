def get_print_current_board(board):
    [print(f"| {' | '.join(el)} |") for el in board]


def is_row_winner(board):
    is_found = False
    for row in board:
        if row.count('x') == len(row) or row.count('O') == len(row):
            is_found = True
    return is_found


def is_col_winner(board):
    check = []
    for row in range(len(board)):
        for col in range(len(board)):
            check.append(board[col][row])
        if check.count('x') == len(board) or check.count('O') == len(board):
            return True
        check = []
    return False


def is_primary_diagonal_first(board):
    check = []
    for row in range(len(board)):
        check.append(board[row][len(board)-1-row])
        if check.count('x') == len(board) or check.count('O') == len(board):
            return True
    return False


def is_primary_diagonal_second(board):
    check = []
    for row in range(len(board)):
        check.append(board[row][row])
        if check.count('x') == len(board) or check.count('O') == len(board):
            return True
    return False


def is_winner(board):
    if is_row_winner(board) or is_col_winner(board) or is_primary_diagonal_first(board) or is_primary_diagonal_second(board):
        return True
    return False


def is_board_ful(board):
    for i in board:
        if " " in i:
            return True
    return False

