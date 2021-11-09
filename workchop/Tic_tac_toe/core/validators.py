from Python_Advanced.workchop.Tic_tac_toe.core.constants import position_mapper


def is_position_in_range(pos):
    if 1 <= pos <= 9:
        return True
    return False


def is_place_available(board, position):
    row, col = position_mapper[position]
    if not board[row][col] == " ":
        return False
    return True