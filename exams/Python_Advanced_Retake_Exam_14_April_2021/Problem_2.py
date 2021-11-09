import math


def is_in_range(r, c):
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


def is_number(n):
    try:
        return int(n)
    except Exception:
        return False


player_1, player_2 = input().split(', ')
line_dict = {player_1: {'score': 501}, player_2: {'score': 501}}
players_red = {0: player_2, 1: player_1}

size = 7
matrix = []

for i in range(size):
    matrix.append([j for j in input().split()])
red = 0


while True:
    row, col = [int(el) for el in input()[1:-1].split(', ')]
    score = 0
    red += 1
    if is_in_range(row, col):
        number = is_number(matrix[row][col])
        if number:
            line_dict[players_red[red % 2]]['score'] -= number

        if not number:
            current_points = sum([
                int(matrix[0][col]),
                int(matrix[-1][col]),
                int(matrix[row][0]),
                int(matrix[row][-1])
            ])
            if matrix[row][col] == "D":
                line_dict[players_red[red % 2]]['score'] -= current_points * 2
            elif matrix[row][col] == "T":
                line_dict[players_red[red % 2]]['score'] -= current_points * 3
            elif matrix[row][col] == "B":
                line_dict[players_red[red % 2]]['score'] -= 501

    if line_dict[players_red[red % 2]]['score'] <= 0:
        break

print(f"{players_red[red % 2]} won the game with {math.ceil(red/2)} throws!")