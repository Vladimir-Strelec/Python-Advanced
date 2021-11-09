n = int(input())

matrix = [[int(col) for col in input().split()] for row in range(n)]
first = []
second = []

for row in range(n):
    first.append(matrix[row][row])
    second.append(matrix[row][n - 1 - row])
print(f"Primary diagonal: {', '.join([str(el) for el in first])}. Sum: {sum(first)}")
print(f"Secondary diagonal: {', '.join([str(el) for el in second])}. Sum: {sum(second)}")

