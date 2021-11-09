from Python_Advanced.workchop.Tic_tac_toe.core.constants import position_mapper
from Python_Advanced.workchop.Tic_tac_toe.core.helper import get_print_current_board, is_winner, is_board_ful
from Python_Advanced.workchop.Tic_tac_toe.core.validators import is_position_in_range, is_place_available


def play(player, board, turns):
    current_turn_count = 1

    while True:
        current_player_name = turns[current_turn_count % 2]
        position = int(input(f"{current_player_name} choose free position: "))

        if is_position_in_range(position):
            if is_place_available(board, position):
                row, col = position_mapper[position]
                board[row][col] = player[current_player_name]
                get_print_current_board(board)
                if is_winner(board):
                    print(f"{current_player_name} wins!")
                    exit(0)
                if not is_board_ful(board):
                    print("Board full")
                    exit(0)
        else:
            pass
        current_turn_count += 1