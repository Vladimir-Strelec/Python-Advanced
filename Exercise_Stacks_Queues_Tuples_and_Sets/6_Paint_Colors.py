from collections import deque
substrings = deque(input().split())

Main_colors = {'red', 'yellow', 'blue'}
Secondary_colors = {'orange': ['red', 'yellow'], 'purple': ['red', 'blue'], 'green': ['yellow', 'blue']}

collections_colors = []

while substrings:
    left = substrings.popleft()
    right = substrings.pop() if substrings else ''
    color = left + right
    if color in Main_colors or color in Secondary_colors:
        collections_colors.append(color)
        continue
    color = right + left
    if color in Main_colors or color in Secondary_colors:
        collections_colors.append(color)
    else:
        left, right = left[:-1], right[:-1]
        if left: substrings.insert(len(substrings)//2, left)
        if right: substrings.insert(len(substrings)//2, right)


for i in collections_colors:
    if i in Secondary_colors:
        if set(Secondary_colors[i]).issubset(collections_colors):
            continue
        else:
            collections_colors = [j for j in collections_colors if j != i]
print(collections_colors)