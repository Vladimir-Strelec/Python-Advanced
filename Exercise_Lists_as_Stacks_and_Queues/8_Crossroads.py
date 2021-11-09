from collections import deque

grin_light = int(input())
chek = True
window = int(input())
command = input()

stack = deque()
count_cars = 0
auto = ''
while not command == "END":
    if command == "green":
        time_light = grin_light
        current_auto = deque(stack.popleft())
        auto = ''
        while time_light:
            if time_light >= len(current_auto):
                time_light -= len(current_auto)
                continue
            elif time_light < len(current_auto):
                len_auto = len(current_auto) - time_light
                time_light = 0
                chek = True
            else:
                count_cars += 1
                if stack:
                    current_auto = deque(stack.popleft())

                else:
                    chek = False
                    break

        while window and chek:
            if len_auto < window:
                window -= len_auto
                count_cars += 1
                break
            else:
                print('A crash happened!')
                print(f'{stack.popleft()} was hit at e.')
                exit()

    else:
        stack.append(command)
    command = input()
print('Everyone is safe.')
print(f'{count_cars} total cars passed the crossroads.')