def get_range(r, c):
    if r in range(size) and c in range(size):
        return True
    return False


def get_current_battle(row, col, i):
    global won
    if get_range(row, col + i) and line_dict['right']:
        if matrix[row][col + i] == "Q":
            print([row, col + i])
            line_dict['right'] = False
            won = True

    if get_range(row, col-i) and line_dict['left']:
        if matrix[row][col-i] == "Q":
            print([row, col-i])
            line_dict['left'] = False
            won = True
    if get_range(row-i, col) and line_dict['up']:
        if matrix[row-i][col] == "Q":
            print([row-i, col])
            line_dict['up'] = False
            won = True
    if get_range(row+i, col) and line_dict['down']:
        if matrix[row + i][col] == "Q":
            print([row + i, col])
            line_dict['down'] = False
            won = True
        ########################
    if get_range(row-i, col - i) and line_dict['up_L']:
        if matrix[row - i][col - i] == "Q":
            print([row - i, col - i])
            line_dict['up_L'] = False
            won = True
    if get_range(row - i, col + i) and line_dict['up_R']:
        if matrix[row - i][col + i] == "Q":
            print([row - i, col + i])
            line_dict['up_R'] = False
            won = True
    if get_range(row + i, col - i) and line_dict['down_L']:
        if matrix[row + i][col - i] == "Q":
            print([row + i, col - i])
            line_dict['down_L'] = False
            won = True
    if get_range(row + i, col + i) and line_dict['down_R']:
        if matrix[row + i][col + i] == "Q":
            print([row + i, col + i])
            line_dict['down_R'] = False
            won = True


size = 8
matrix = []
king_row, king_col = 0, 0
for i in range(size):
    element = input().split()
    matrix.append(element)
    for j in range(len(element)):
        if element[j] == "K":
            king_row, king_col = i, j

line_dict = {
    "up": True,
    "down": True,
    "left": True,
    "right": True,
    ########################
    "up_L": True,
    "up_R": True,
    "down_L": True,
    "down_R": True,
}
won = None
i = 1
while i <= size:

    get_current_battle(king_row, king_col, i)
    i += 1

if won is None:
    print('The king is safe!')
    exit(0)