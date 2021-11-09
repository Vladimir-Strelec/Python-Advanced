from collections import deque


def is_inside(r, c):
    return 0 <= r < rows and 0 <= c < cols


def get_next_position(direction, row, col):
    if direction == "U":
        return (row - 1, col)
    if direction == "D":
        return (row + 1, col)
    if direction == "L":
        return (row, col - 1)
    if direction == "R":
        return (row, col + 1)


def get_next_bunnies(bunnies, rows, cols):
    next_bunnies = []
    for r, c in bunnies:
        if is_inside(rows, cols, r - 1, c):
            next_bunnies.append([r - 1, c])
        if is_inside(rows, cols, r + 1, c):
            next_bunnies.append([r + 1, c])
        if is_inside(rows, cols, r, c - 1):
            next_bunnies.append([r, c - 1])
        if is_inside(rows, cols, r, c + 1):
            next_bunnies.append([r, c + 1])
    return next_bunnies


rows, cols = [int(el) for el in input().split()]

matrix = []
player_row = 0
player_col = 0

bunnies = []

for row in range(rows):
    row_elements = list(input())
    matrix.append(row_elements)
    for col in range(cols):
        el = row_elements[col]
        if el == "P":
            player_row, player_col = row, col
        elif el == "B":
            bunnies.append([row, col])


won = None
commands = deque(input())
matrix[player_row][player_col] = '.'

while commands:
    command = commands.popleft()
    next_player_row, next_player_col = get_next_position(command, player_row, player_col)
    if not is_inside(next_player_row, next_player_col):
        won = True
    elif matrix[next_player_row][next_player_col] == 'B':
        won = False
    if not won:
        player_row, player_col = next_player_row, next_player_col

    next_bunnies = get_next_bunnies(bunnies, rows, cols)

    for r, c in next_bunnies:
        if r == player_row and c == player_col and not won:
            won = False
        matrix[r][c] = 'B'
    bunnies += next_bunnies
    if won == True or won == False:
        break

for i in matrix:
    print(''.join(i))

if won:
    print(f'won: {player_row} {player_col}')
else:
    print(f'dead: {player_row} {player_col}')







#
# from collections import deque
#
#
# def check_player(r, c, com):
#     global x, y, rows, cols
#     if com == 'L' and c - 1 in range(cols):
#         matrix[x][y] = '.'
#         y -= 1
#         return True
#     elif com == 'R' and c + 1 in range(cols):
#         matrix[x][y] = '.'
#         y += 1
#         return True
#     elif com == 'U' and r - 1 in range(rows):
#         matrix[x][y] = '.'
#         x -= 1
#         return True
#     elif com == 'D' and r + 1 in range(rows):
#         matrix[x][y] = '.'
#         x += 1
#         return True
#     else:
#         return False
#
#
# def vampire(x_v, y_v):
#     global rows, cols
#     stack_x = []
#     stack_y = []
#     if y_v - 1 in range(cols):
#         stack_y.append(y_v - 1)
#         stack_x.append(x_v)
#     if y_v + 1 in range(cols):
#         stack_y.append(y_v + 1)
#         stack_x.append(x_v)
#     if x_v - 1 in range(rows):
#         stack_y.append(y_v)
#         stack_x.append(x_v-1)
#     if x_v + 1 in range(rows):
#         stack_y.append(y_v)
#         stack_x.append(x_v+1)
#
#     return [deque(stack_x), deque(stack_y)]
#
#
# def position_vampire(r, c):
#     while r:
#         x_el = r.popleft()
#         y_el = c.popleft()
#         matrix[x_el][y_el] = 'B'
#
#
# rows, cols = [int(el) for el in input().split()]
# matrix = [[j for j in input()]for i in range(rows)]
# command = deque([el for el in input()])
#
# x = [i for j in range(cols) for i in range(rows) if matrix[i][j] == 'P'][0]
# y = [j for j in range(cols) for i in range(rows) if matrix[i][j] == 'P'][0]
#
# x_B = [i for j in range(cols) for i in range(rows) if matrix[i][j] == 'B']
# y_B = [j for j in range(cols) for i in range(rows) if matrix[i][j] == 'B']
# check_bul = True
# while command and check_bul:
#     start = command.popleft()
#     result_player = check_player(x, y, start)
#     if result_player:
#         matrix[x][y] = 'P'
#     else:
#         check_bul = False
#         matrix[x][y] = '.'
#
#     count_vampire = [vampire(i, j) for i in range(rows) for j in range(cols) if matrix[i][j] == 'B']
#     for i in count_vampire:
#         position_vampire(i[0], i[1])
#
#     if matrix[x][y] == 'B':
#
#         check_bul = True
#         break
#
#
# for l in matrix:
#     print(''.join(l))
# if not check_bul or len(command) == 0:
#     print(f'won: {x} {y}')
# else:
#     if command:
#         print(f'dead: {x} {y}')