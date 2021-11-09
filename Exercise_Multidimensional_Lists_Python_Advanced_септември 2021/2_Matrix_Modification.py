def is_valid(matr, r, c):
    if r in range(len(matr)) and c in range(len(matr)):
        return True
    else:
        return False


rows_and_cols = int(input())
matrix = [[int(j) for j in input().split()] for i in range(rows_and_cols)]
command = input()
while not command == 'END':
    command = command.split()
    if command[0] == 'Add' and is_valid(matrix, int(command[1]), int(command[2])):
        matrix[int(command[1])][int(command[2])] += int(command[3])
    elif command[0] == 'Subtract' and is_valid(matrix, int(command[1]), int(command[2])):
        matrix[int(command[1])][int(command[2])] -= int(command[3])
    else:
        print('Invalid coordinates')
    command = input()

for r in matrix:
    for c in r:
        print(''.join(str(c)), end=' ')
    print()