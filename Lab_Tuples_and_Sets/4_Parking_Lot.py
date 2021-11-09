num = int(input())

garage = set()

for i in range(num):
    command, num_cars = input().split(', ')
    if command == "IN":
        garage.add(num_cars)
    elif command == "OUT":
        garage.discard(num_cars)

if len(garage) > 0:
    print('\n'.join(garage))
else:
    print("Parking Lot is Empty")