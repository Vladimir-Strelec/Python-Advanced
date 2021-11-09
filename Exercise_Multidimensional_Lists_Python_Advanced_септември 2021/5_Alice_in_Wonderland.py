def is_valid(m, r, c):
    if r in range(len(m)) and c in range(len(m)):
        return True
    return False


def direction(m, position_x, position_y):
    if is_valid(m, position_x, position_y):
        if not m[position_x][position_y] == "R":
            return [position_x, position_y]
        else:
            m[position_x][position_y] = '*'
            return False
    return False


size = int(input())
matrix = []
alice_position_x, alice_position_y = 0, 0
count_ticket = 0
for i in range(size):
    element = input().split()
    matrix.append(element)
    for j in range(size):
        if matrix[i][j] == 'A':
            alice_position_x, alice_position_y, count_ticket = i, j, 0

command = input()
while command:
    matrix[alice_position_x][alice_position_y] = '*'
    if command == 'down':
        result = direction(matrix, alice_position_x + 1, alice_position_y)
        if result:
            alice_position_x, alice_position_y = result[0], result[1]
            if matrix[alice_position_x][alice_position_y].isdigit():
                count_ticket += int(matrix[alice_position_x][alice_position_y])
            matrix[alice_position_x][alice_position_y] = '*'
        else:
            break

    elif command == 'right':
        result = direction(matrix, alice_position_x, alice_position_y+1)
        if result:
            alice_position_x, alice_position_y = result[0], result[1]
            if matrix[alice_position_x][alice_position_y].isdigit():
                count_ticket += int(matrix[alice_position_x][alice_position_y])
            matrix[alice_position_x][alice_position_y] = '*'
        else:
            break

    elif command == 'up':
        result = direction(matrix, alice_position_x-1, alice_position_y)
        if result:
            alice_position_x, alice_position_y = result[0], result[1]
            if matrix[alice_position_x][alice_position_y].isdigit():
                count_ticket += int(matrix[alice_position_x][alice_position_y])
            matrix[alice_position_x][alice_position_y] = '*'
        else:
            break

    elif command == 'left':
        result = direction(matrix, alice_position_x, alice_position_y-1)
        if result:
            alice_position_x, alice_position_y = result[0], result[1]
            if matrix[alice_position_x][alice_position_y].isdigit():
                count_ticket += int(matrix[alice_position_x][alice_position_y])
            matrix[alice_position_x][alice_position_y] = '*'
        else:
            break
    if count_ticket >= 10:
        break
    command = input()
if count_ticket >= 10:
    print('She did it! She went to the party.')
else:
    print("Alice didn't make it to the tea party.")
for i in matrix:
    print(" ".join(i))