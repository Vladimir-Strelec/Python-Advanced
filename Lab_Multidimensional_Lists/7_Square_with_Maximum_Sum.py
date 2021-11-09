import sys
row, col = [int(el) for el in input().split(", ")]

matrix = [[int(j) for j in input().split(", ")] for i in range(row)]
max_sum = - sys.maxsize
position = None
for r in range(row-1, 0, -1):
    for c in range(col-1, 0, -1):
        current_sum = matrix[r][c] + matrix[r][c-1] + matrix[r-1][c] + matrix[r-1][c-1]
        if current_sum >= max_sum:
            max_sum = current_sum
            position = (r, c)
r, c = position
print(matrix[r-1][c-1], matrix[r-1][c])
print(matrix[r][c-1], matrix[r][c])
print(max_sum)