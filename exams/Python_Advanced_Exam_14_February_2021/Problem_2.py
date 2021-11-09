from math import ceil


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
count_step = []
gold = 0
won = False

size = int(input())
matrix = []
for i in range(size):
    element = input().split()
    matrix.append(element)
    for j in range(size):
        if matrix[i][j] == 'P': player_position_row, player_position_col = i, j


while gold < 100:
    direction = input()
    new_pos_row, new_pos_col = get_position(direction, player_position_row, player_position_col)

    if is_range_size(new_pos_row, new_pos_col):
        won = True
        break
    if matrix[new_pos_row][new_pos_col] == 'X':
        won = True
        break

    if not matrix[new_pos_row][new_pos_col].isalpha():
        gold += int(matrix[new_pos_row][new_pos_col])
        count_step.append([new_pos_row, new_pos_col])
        player_position_row, player_position_col = new_pos_row, new_pos_col

if won:
    gold -= gold * 0.50
    print(f"Game over! You've collected {int(gold)} coins.")

else:
    print(f"You won! You've collected {int(gold)} coins.")

print('Your path:')
print('\n'.join([str(i) for i in count_step]))

