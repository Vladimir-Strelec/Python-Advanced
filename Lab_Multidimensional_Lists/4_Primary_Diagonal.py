matrix = [[int(j) for j in input().split()] for i in range(int(input()))]
print(sum([matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix[i])) if i == j]))

