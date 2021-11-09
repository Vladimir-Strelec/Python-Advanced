row, column = [int(el) for el in input().split(", ")]

matrix = [[int(j) for j in input().split(", ")] for i in range(row)]
count = [sum(i) for i in matrix]

print(sum(count))
print(matrix)