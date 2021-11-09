from collections import deque
chocolate_line = deque(input().split(', '))
milk_line = deque(input().split(', '))
count = 0

while chocolate_line and milk_line and count < 5:
    current_chocolate = int(chocolate_line.pop())
    current_milk = int(milk_line.popleft())
    if current_chocolate == current_milk:
        count += 1

    elif current_chocolate <= 0 and current_milk > 0:
        milk_line.appendleft(str(current_milk))

    elif current_milk <= 0 and current_chocolate > 0:
        chocolate_line.append(str(current_chocolate))

    elif current_milk <= 0 and current_chocolate <= 0:
        pass
    else:
        milk_line.append(str(current_milk))
        current_chocolate = current_chocolate - 5
        chocolate_line.append(str(current_chocolate))

if count == 5:
    print(f"Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolate_line:
    print(f"Chocolate: {', '.join([i for i in chocolate_line])}")
else:
    print('Chocolate: empty')

if milk_line:
    print(f"Milk: {', '.join([i for i in milk_line])}")
else:
    print('Milk: empty')