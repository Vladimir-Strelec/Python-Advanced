from collections import deque


def fill_the_box(*args):
    height, length, width = args[:3]
    size = height * length * width
    stack = deque()
    for i in range(3, len(args)):
        if args[i] != 'Finish':
            stack.append(args[i])
        else:
            break
    while stack:
        current_box = stack.popleft()
        if current_box > size:
            current_box -= size
            size = 0
            stack.appendleft(current_box)
            break
        else:
            size -= current_box
    if size > 0:
        return f"There is free space in the box. You could put {size} more cubes."
    else:
        return f"No more free space! You have {sum(stack)} more cubes."


print(fill_the_box(10, 10, 10, 40, 'Finish', 2, 15, 30))