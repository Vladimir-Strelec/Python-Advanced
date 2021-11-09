n = int(input())

matrix = [[int(j) for j in input().split()] for i in range(n)]

print(abs(sum([matrix[row][row] for row in range(n)]) - sum([matrix[row][n - 1 - row] for row in range(n)])))

