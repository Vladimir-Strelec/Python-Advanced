from collections import deque
COMMAND_START = "Start"
COMMAND_END = 'End'
COMMAND_REFILL = 'refill'

quantity_water = int(input())
line_people = deque()

while True:
    command = input()
    if command == COMMAND_START:
        break
    line_people.append(command)

while True:
    command = input()
    if command == COMMAND_END:
        break
    elif COMMAND_REFILL in command:
        command = command.split()
        quantity_water += int(command[1])
        continue
    if int(command) <= quantity_water:
        quantity_water -= int(command)
        print(f"{line_people.popleft()} got water")
    else:
        print(f"{line_people.popleft()} must wait")
print(f"{quantity_water} liters left")