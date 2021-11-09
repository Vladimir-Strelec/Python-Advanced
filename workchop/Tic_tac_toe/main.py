from Python_Advanced.workchop.Tic_tac_toe.core.logik import play


def print_initial_board_positional(p):
    print("This is the numeration of the board")
    print("| 1 | 2 | 3 |")
    print("| 4 | 5 | 6 |")
    print("| 7 | 8 | 9 |")
    print(f"{p} Starts first")


def create_empty_board():
    return [[" " for _ in range(3)] for _ in range(3)]


def setup():
    player_1 = input('Player 1 name: ')
    player_2 = input('Player 2 name: ')
    player_1_sign = input(f"{player_1} would you like to play with 'X' or 'O'?")
    while player_1_sign.upper() not in ['X', 'O']:
        player_1_sign = input(f"{player_1} would you like to play with 'X' or 'O'?")
    player_2_sign = "O" if player_1_sign.upper() == "X" else "X"
    print_initial_board_positional(player_1)
    board = create_empty_board()
    players = {player_1: player_1_sign, player_2: player_2_sign}
    turns_mapper = {0: player_2, 1: player_1}
    play(players, board, turns_mapper)


def start_game():
    setup()


if __name__ == "__main__":
    start_game()