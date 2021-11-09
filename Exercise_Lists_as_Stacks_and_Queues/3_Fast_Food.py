from collections import deque

quantity_food = int(input())
stack = deque(input().split())
if len(stack) > 0:
    print(max(list(map(int, stack))))
while stack:
    if int(stack[0]) <= quantity_food:
        x = int(stack.popleft())
        quantity_food -= x
    else:
        print(f"Orders left: {' '.join(stack)}")
        exit()
print('Orders complete')