from collections import deque

line_kid = deque(input().split())
jump = int(input())
i = 0
while line_kid:
    if i == jump:
        if len(line_kid) == 1:
            print(f"Last is {line_kid.pop()}")
            exit()
        print(f"Removed {line_kid.pop()}")
        i = 0
    elif i < jump:
        x = line_kid.popleft()
        line_kid.append(x)
        i += 1

