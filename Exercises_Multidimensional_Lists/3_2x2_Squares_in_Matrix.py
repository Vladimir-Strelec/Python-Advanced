rows, cols = [int(i) for i in input().split()]

matrix = [[j for j in input().split()] for i in range(rows)]
count = 0

for row in range(rows - 1):
    for col in range(cols - 1):
        check = matrix[row][col] + matrix[row][col + 1] + matrix[row + 1][col] + matrix[row + 1][col + 1]
        if matrix[row][col] == matrix[row][col+1] == matrix[row+1][col] == matrix[row+1][col+1]:
            count += 1
print(count)