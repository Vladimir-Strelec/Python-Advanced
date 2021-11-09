n = int(input())
matrix = []
for i in range(n):
    matrix.append([int(j) for j in input().split()])

matrix_bomb = tuple([i.split(",") for i in input().split()])
for i in matrix_bomb:
    row, col = i[:]
    row, col = int(row), int(col)

    amount_bomb = matrix[row][col]
    matrix[row][col] -= amount_bomb
    if col-1 in range(n) and row in range(n) and matrix[row][col-1] > 0: matrix[row][col-1] -= amount_bomb
    if col+1 in range(n) and row in range(n) and matrix[row][col+1] > 0: matrix[row][col+1] -= amount_bomb
    if col-1 in range(n) and row-1 in range(n) and matrix[row-1][col-1] > 0: matrix[row-1][col-1] -= amount_bomb
    if col+1 in range(n) and row+1 in range(n) and matrix[row+1][col+1] > 0: matrix[row+1][col+1] -= amount_bomb
    if col-1 in range(n) and row+1 in range(n) and matrix[row+1][col-1] > 0: matrix[row+1][col-1] -= amount_bomb
    if col+1 in range(n) and row-1 in range(n) and matrix[row-1][col+1] > 0: matrix[row-1][col+1] -= amount_bomb
    if row+1 in range(n) and row+1 in range(n) and matrix[row + 1][col] > 0: matrix[row + 1][col] -= amount_bomb
    if row-1 in range(n) and row-1 in range(n) and matrix[row - 1][col] > 0: matrix[row - 1][col] -= amount_bomb

summa = [j for i in matrix for j in i if j > 0]

print(f"Alive cells: {len(summa)}")
print(f"Sum: {sum(summa)}")

for i in matrix:
    for j in i:
        print(j, end=" ")
    print()