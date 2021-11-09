from collections import deque
stack = deque()
count_column = int(input())


start = 0
for i in range(count_column):
    stack.append(list(map(int, input().split())))

while stack:
    BACK = 0
    count = 0
    for i in stack:
        if BACK + i[0] >= i[1]:
            BACK += i[0] - i[1]
            count += 1
            if count == len(stack):
                print(start)
                exit()
        else:
            stack.rotate(-1)
            start += 1
            break
