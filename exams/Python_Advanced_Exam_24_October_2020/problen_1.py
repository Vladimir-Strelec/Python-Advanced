from collections import deque
tasks = [int(el) for el in input().split(', ')]
searched_index = int(input())
result = 0
cycles = deque(sorted([(tasks[index], index) for index in range(len(tasks))]))

while cycles:
    number, index = cycles.popleft()
    result += number
    if index == searched_index:
        print(result)
        exit(0)