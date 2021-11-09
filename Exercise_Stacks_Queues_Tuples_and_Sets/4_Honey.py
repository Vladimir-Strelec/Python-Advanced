from collections import deque
working_bees = deque([int(i) for i in input().split()])
nectar = [int(i) for i in input().split()]
line_command = deque(input().split())
total = 0

while working_bees and nectar:
    current_bee = working_bees.popleft()
    current_nectar = nectar.pop()

    if current_nectar >= current_bee:
        current_command = line_command.popleft()
        if current_command == "+":
            total += abs(current_bee + current_nectar)
        elif current_command == "-":
            total += abs(current_bee - current_nectar)
        elif current_command == "*":
            total += abs(current_bee * current_nectar)
        elif current_command == "/":
            if current_nectar > 0:
                total += abs(current_bee / current_nectar)
    else:
        working_bees.appendleft(current_bee)

print(f"Total honey made: {total}")
if working_bees:
    print(f"Bees left: {', '.join(list(map(str, working_bees)))}")
if nectar:
    print(f"Nectar left: {', '.join(list(map(str, nectar)))}")

