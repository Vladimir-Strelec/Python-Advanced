def get_in_range(rov, col):
    if 0 <= rov <= n and 0 <= col <= n:
        return True
    return False


def get_position_player(com, r, c):
    line_dict = {
        'up': (r-1, c),
        'down': (r+1, c),
        'right': (r, c+1),
        'left': (r, c-1),
    }
    return line_dict[com]


word = input()
n = int(input())
matrix = []
position_player_row, position_player_col = (0, 0)

for i in range(n):
    element = list(map(str, input()))
    matrix.append(element)
    for j in range(n):
        if matrix[i][j] == "P":
            position_player_row, position_player_col = i, j

count_n = int(input())
for _ in range(count_n):
    command = input()

    new_position_row, new_position_col = get_position_player(command, position_player_row, position_player_col)
    if get_in_range(new_position_row, new_position_col):

        if matrix[new_position_row][new_position_col].isalpha():
            word += (matrix[new_position_row][new_position_col])

        matrix[new_position_row][new_position_col] = 'P'
        matrix[position_player_row][position_player_col] = "-"
        position_player_row, position_player_col = new_position_row, new_position_col
    else:
        if word:
            word = word[:-1]


print(word)
print("\n".join([''.join(i) for i in matrix]))
