row, col = [int(el) for el in input().split(", ")]

matrix = [[int(j) for j in input().split()] for i in range(row)]
count = [[matrix[j][i] for j in range(row)]for i in range(col)]


print('\n'.join([str(sum(num)) for num in count]))


# for i in range(col):
#     x = []
#     for j in range(row):
#         x.append(matrix[j][i])
