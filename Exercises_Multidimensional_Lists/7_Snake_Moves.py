rows, cols = [int(el) for el in input().split()]
animal = input()
matrix = []
animal_idx = 0
for row in range(rows):
    matrix.append([None]*cols)
    for col in range(cols):
        if row % 2 == 0:
            matrix[row][col] = animal[animal_idx]
        else:
            matrix[row][cols - 1 - col] = animal[animal_idx]
        animal_idx = (animal_idx + 1) % len(animal)

for i in matrix:
    print("".join(list(map(str, i))))