rows, cols = [int(el) for el in input().split()]

matrix = [[int(col) for col in input().split()]for row in range(rows)]
summa = 0
position = None

for row in range(rows-1, 1, -1):
    for col in range(cols-1, 1, -1):
        check = matrix[row][col] + matrix[row][col-1] + matrix[row][col-2] + \
                matrix[row-1][col] + matrix[row-1][col-1] + matrix[row-1][col-2] + \
                matrix[row-2][col] + matrix[row-2][col-1] + matrix[row-2][col-2]

        if check >= summa:
            summa = check
            position = (row, col)

r, c = position
print(f"Sum = {summa}")
print(f'{matrix[r-2][c-2]} {matrix[r-2][c-1]} {matrix[r-2][c]}')
print(f'{matrix[r-1][c-2]} {matrix[r-1][c-1]} {matrix[r-1][c]}')
print(f'{matrix[r][c-2]} {matrix[r][c-1]} {matrix[r][c]}')