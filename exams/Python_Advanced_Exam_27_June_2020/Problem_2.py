def is_range_size(pos_row, pos_col):
    if pos_row not in range(size) or pos_col not in range(size):
        return True
    return False


def get_position(d, row, col):
    if d == 'up': return (row-1, col)
    elif d == 'down': return (row+1, col)
    elif d == 'left': return (row, col-1)
    elif d == 'right': return (row, col+1)


player_position_row, player_position_col = 0, 0
position_pit = []
count_step = []
food = 0
won = False

size = int(input())
matrix = []
for i in range(size):
    element = list(map(str, input()))
    matrix.append(element)
    for j in range(len(element)):
        if element[j] == 'S': player_position_row, player_position_col = i, j
        if element[j] == 'B': position_pit.append((i, j))
a=5

while food < 10:
    direction = input()
    new_pos_row, new_pos_col = get_position(direction, player_position_row, player_position_col)

    if is_range_size(new_pos_row, new_pos_col):
        matrix[player_position_row][player_position_col] = '.'
        print('Game over!')
        won = True
        break
    if matrix[new_pos_row][new_pos_col] == 'B':
        matrix[new_pos_row][new_pos_col] = '.'
        if new_pos_row == position_pit[0][0] and new_pos_col == position_pit[0][1]:
            new_pos_row, new_pos_col = position_pit[1][0], position_pit[1][1]
        else:
            new_pos_row = position_pit[0][0], new_pos_col = position_pit[0][1]

    if not matrix[new_pos_row][new_pos_col].isalpha() and matrix[new_pos_row][new_pos_col] == "*":
        food += 1
    matrix[player_position_row][player_position_col] = '.'
    player_position_row, player_position_col = new_pos_row, new_pos_col
    matrix[player_position_row][player_position_col] = 'S'
if not won:
    print('You won! You fed the snake.')
print(f"Food eaten: {food}")
for i in matrix:
    print("".join(i))