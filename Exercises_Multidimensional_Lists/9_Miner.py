from collections import deque


def check_range(matr, r, c, com):
    global x, y
    if com == 'left' and c-1 in range(len(matr)):
        y -= 1
        return True
    elif com == 'right' and c+1 in range(len(matr)):
        y += 1
        return True
    elif com == 'up' and r-1 in range(len(matr)):
        x -= 1
        return True
    elif com == 'down' and r+1 in range(len(matr)):
        x += 1
        return True
    else:
        return False


n = int(input())
command = deque(tuple(input().split()))
matrix = [[j for j in input().split()] for i in range(n)]

x = [i for i in range(n) for j in range(n) if matrix[i][j] == 's'][0]
y = [j for i in range(n) for j in range(n) if matrix[i][j] == 's'][0]
coal = len([1 for i in range(n) for j in range(n) if matrix[i][j] == 'c'])

while command:
    start = command.popleft()
    result = check_range(matrix, x, y, start)
    if result:
        if matrix[x][y] == "c":
            matrix[x][y] = "*"
            coal -= 1
            if coal == 0:
                print(f"You collected all coal! ({x}, {y})")
                exit()
        elif matrix[x][y] == "e":
            print(f'Game over! ({x}, {y})')
            exit()
print(f"{coal} pieces of coal left. ({x}, {y})")

