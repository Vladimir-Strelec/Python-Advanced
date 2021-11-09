def not_is_range(santa_r, santa_c):
    if santa_r not in range(size) or santa_c not in range(size):
        return True
    return False


def get_position_santa(direc, row, col):
    if direc == 'up': return row - 1, col
    if direc == 'down': return row + 1, col
    if direc == 'left': return row, col - 1
    if direc == 'right': return row, col + 1


presents = int(input())
size = int(input())
matrix = []

list_command = ['up', 'down', 'left', 'right']
santa_row, santa_col = 0, 0
good_kids = 0
happy_kids = 0

for i in range(size):
    element = input().split()
    matrix.append(element)
    for j in range(size):
        if matrix[i][j] == 'S': santa_row, santa_col = i, j
        if matrix[i][j] == 'V': good_kids += 1


command = input()
while not command == 'Christmas morning':
    nex_santa_row, nex_santa_col = get_position_santa(command, santa_row, santa_col)

    if matrix[nex_santa_row][nex_santa_col] == 'C':
        matrix[nex_santa_row][nex_santa_col] = 'S'
        matrix[santa_row][santa_col] = '-'
        santa_row, santa_col = nex_santa_row, nex_santa_col
        for i in list_command:
            nex_santa_row, nex_santa_col = get_position_santa(i, santa_row, santa_col)
            if matrix[nex_santa_row][nex_santa_col] == 'X':
                presents -= 1
            elif matrix[nex_santa_row][nex_santa_col] == 'V':
                presents -= 1
                good_kids -= 1
                happy_kids += 1
            matrix[nex_santa_row][nex_santa_col] = '-'
            if presents == 0:
                break

    elif matrix[nex_santa_row][nex_santa_col] == 'V':
        presents -= 1
        good_kids -= 1
        happy_kids += 1
        matrix[santa_row][santa_col] = '-'
        matrix[nex_santa_row][nex_santa_col] = 'S'

    elif matrix[nex_santa_row][nex_santa_col] == 'X':
        matrix[santa_row][santa_col] = '-'
        matrix[nex_santa_row][nex_santa_col] = 'S'
    else:
        matrix[santa_row][santa_col] = '-'
        matrix[nex_santa_row][nex_santa_col] = 'S'
    santa_row, santa_col = nex_santa_row, nex_santa_col
    if presents == 0:
        break
    command = input()

if presents == 0 and good_kids > 0:
    print('Santa ran out of presents!')
for i in matrix:
    print(' '.join(i))
if good_kids > 0:
    print(f'No presents for {good_kids} nice kid/s.')
else:
    print(f'Good job, Santa! {happy_kids} happy nice kid/s.')
