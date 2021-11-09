rows, cols = [int(el) for el in input().split()]

for i in range(rows):
        for j in range(cols):
                print(f"{chr(97+i)}{chr(97+j+i)}{chr(97+i)}", end=" ")
        print()