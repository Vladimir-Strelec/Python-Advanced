matrix = [[int(j) for j in input().split(", ")] for i in range(int(input()))]
print([i for j in matrix for i in j])