def check_range(row, col):
    if 0 <= row < size and 0 <= col < size:
        return True
    return False


def check_direction_bomb(r, c, direc):
    line_dict = {
        'up': (r-1, c),
        'down': (r+1, c),
        'left': (r, c-1),
        'right': (r, c+1),
        ##################
        'up_l': (r - 1, c-1),
        'up_r': (r - 1, c+1),
        'down_l': (r+1, c - 1),
        'down_r': (r+1, c + 1),
    }
    if not check_range(line_dict[direc][0], line_dict[direc][1]):
        return False
    else:
        if not matrix[line_dict[direc][0]][line_dict[direc][1]] == '*':
            return False
    return True


size = int(input())
n_bomb = int(input())
matrix = []

for _ in range(size):
    matrix.append([" " for _ in range(size)])
for _ in range(n_bomb):
    r, c = [int(el) for el in input()[1:-1].split(', ')]
    matrix[r][c] = '*'
row, col = 0, 0

direction = ['up', 'down', 'left', 'right', 'up_l', 'up_r', 'down_l', 'down_r']

for i in range(size):
    for j in range(size):
        row, col = i, j
        count = 0
        for direct in direction:
            if matrix[i][j] == '*':
                break
            result = check_direction_bomb(row, col, direct)
            if not result:
                continue
            else:
                count += 1
        if not matrix[i][j] == '*':
            matrix[i][j] = count

for i in matrix:
    print(*i)


