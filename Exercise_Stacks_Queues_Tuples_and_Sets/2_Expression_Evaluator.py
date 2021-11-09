from collections import deque

stack = deque()

line_nums = deque(input().split())
while line_nums:
    current_chr = line_nums.popleft()
    if current_chr[-1].isdigit():
        stack.append(current_chr)
    else:
        while len(stack) > 1:
            if current_chr == "-":
                stack.appendleft(int(stack.popleft()) - int(stack.popleft()))
            elif current_chr == "+":
                stack.appendleft(int(stack.popleft()) + int(stack.popleft()))
            elif current_chr == "*":
                stack.appendleft(int(stack.popleft()) * int(stack.popleft()))
            elif current_chr == "/":
                stack.appendleft(int(stack.popleft()) // int(stack.popleft()))
print(stack[0])
