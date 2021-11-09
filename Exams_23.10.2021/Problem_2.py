def get_range(m, r, c):
    return 0 <= r < m and 0 <= c < m


def get_score(m, row, col):
    count = 0
    if m[0][col].isdigit():
        count += int(m[0][col])
    if m[1][col].isdigit():
        count += int(m[1][col])
    if m[2][col].isdigit():
        count += int(m[2][col])
    if m[3][col].isdigit():
        count += int(m[3][col])
    if m[4][col].isdigit():
        count += int(m[4][col])
    if m[5][col].isdigit():
        count += int(m[5][col])
    return count


size = 6
matrix = []

for i in range(size):
    matrix.append(input().split())

vedro = True
point = 0
for _ in range(3):
    command = ' '.join(input().split(', '))
    command = command[1: -1].split()

    position_row, position_col = int(command[0]), int(command[1])
    if not get_range(size, position_row, position_col):
        continue
    if matrix[position_row][position_col] != "B" :
        continue

    else:
        point += get_score(matrix, position_row, position_col)
        matrix[position_row][position_col] = 0
    if point >= 300:
        break
if 100 <= point <= 199:
    print(f"Good job! You scored {point} points, and you've won {'Football'}.")
elif 200 <= point <= 299:
    print(f"Good job! You scored {point} points, and you've won {'Teddy Bear'}.")
elif point >= 300:
    print(f"Good job! You scored {point} points, and you've won {'Lego Construction Set'}.")
else:
    print(f"Sorry! You need {100 - point} points more to win a prize.")