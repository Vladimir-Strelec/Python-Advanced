def is_valid(m, row, col):
    if row in range(len(m)) and col in range(len(m)):
        if not m[row][col] == 'X':
            return True
        return False
    return False


def go_to_up(matr, r, c):
    ex = 0
    steps = []
    direction = 'up'
    for i in range(1, len(matr)+1):
        if is_valid(matr, r-i, c):
            ex += int(matr[r-i][c])
            steps.append((r-i, c))
        else:
            break
    return ex, steps, direction


def go_to_down(matr, r, c):
    ex = 0
    steps = []
    direction = 'down'
    for i in range(1, len(matr)+1):
        if is_valid(matr, r+i, c):
            ex += int(matr[r+i][c])
            steps.append((r+i, c))
        else:
            break
    return ex, steps, direction


def go_to_left(matr, r, c):
    ex = 0
    steps = []
    direction = 'left'
    for i in range(1, len(matr)+1):
        if is_valid(matr, r, c-i):
            ex += int(matr[r][c-i])
            steps.append((r, c-i))
        else:
            break
    return ex, steps, direction


def go_to_right(matr, r, c):
    ex = 0
    steps = []
    direction = 'right'
    for i in range(1, len(matr)+1):
        if is_valid(matr, r, c+i):
            ex += int(matr[r][c+i])
            steps.append((r, c+i))
        else:
            break
    return ex, steps, direction


size = int(input())
matrix = []

bunny_position_x = 0
bunny_position_y = 0
for i in range(size):
    element = input().split()
    matrix.append(element)
    for j in range(size):
        if matrix[i][j] == 'B':
            bunny_position_x, bunny_position_y = i, j

count_ex = 0
list_steps = []
res_direction = ''
while True:

    ex, steps, direct = go_to_up(matrix, bunny_position_x, bunny_position_y)
    if ex >= count_ex:
        count_ex, list_steps, res_direction = ex, steps, direct

    ex, steps, direct = go_to_down(matrix, bunny_position_x, bunny_position_y)
    if ex >= count_ex:
        count_ex, list_steps, res_direction = ex, steps, direct

    ex, steps, direct = go_to_left(matrix, bunny_position_x, bunny_position_y)
    if ex >= count_ex:
        count_ex, list_steps, res_direction = ex, steps, direct

    ex, steps, direct = go_to_right(matrix, bunny_position_x, bunny_position_y)
    if ex >= count_ex:
        count_ex, list_steps, res_direction = ex, steps, direct
    break


print(res_direction)
for i in list_steps:
    for j in range(0, len(i), 2):
        print(f"[{i[j]}, {i[j+1]}]")
print(count_ex)