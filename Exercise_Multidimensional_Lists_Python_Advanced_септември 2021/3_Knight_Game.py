def is_atack(m, curr_r, curr_col):
    if curr_r not in range(len(m)) or curr_col not in range(len(m)):
        return False
    return m[curr_r][curr_col] == 'K'


def count_affected_knights(board, row, col):
    result = 0
    if is_atack(board, row - 2, col - 1):
        result += 1
    if is_atack(board, row - 2, col + 1):
        result += 1
    if is_atack(board, row + 2, col - 1):
        result += 1
    if is_atack(board, row + 2, col + 1):
        result += 1

    if is_atack(board, row - 1, col - 2):
        result += 1
    if is_atack(board, row - 1, col + 2):
        result += 1
    if is_atack(board, row + 1, col - 2):
        result += 1
    if is_atack(board, row + 1, col + 2):
        result += 1
    return result


size = int(input())
matrix = [[j for j in input()] for i in range(size)]

remove = 0
while True:
    max_count, knight_row, knight_col = 0, 0, 0
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == '0':
                continue

            count = count_affected_knights(matrix, r, c)
            if count > max_count:
                max_count, knight_row, knight_col = count, r, c
    if max_count == 0:
        break
    else:
        matrix[knight_row][knight_col] = '0'
        remove += 1
print(remove)
