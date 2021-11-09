rows, cols = [int(el) for el in input().split()]

matrix = [[j for j in input().split()] for i in range(rows)]

command = input()
while not command == "END":
    command = command.split()
    if "swap" in command and len(command) == 5:
        row, col, row_1, col_1 = command[1:]
        row, col, row_1, col_1 = int(row), int(col), int(row_1), int(col_1)

        if row in range(rows) and col in range(cols) and row_1 in range(rows) and col_1 in range(cols):
            matrix[row][col], matrix[row_1][col_1] = matrix[row_1][col_1], matrix[row][col]
            for i in matrix:
                for j in i:
                    print(j, end=" ")
                print()
        else:
            print('Invalid input!')
    else:
        print('Invalid input!')
    command = input()
