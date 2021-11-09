row_col = int(input())

matrix = [[j for j in input()] for i in range(row_col)]
character = input()
chek = []
for i in range(row_col):
    for j in range(row_col):
        if matrix[i][j] == character:
            chek = f"({i}, {j})"
            print(chek)
            exit()

print(f"{character} does not occur in the matrix")