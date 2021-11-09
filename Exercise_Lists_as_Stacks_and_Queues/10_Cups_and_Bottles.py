from collections import deque
capacity_of_cups = deque(map(int, input().split()))
bottle_capacity = deque(map(int, input().split()))

water_left = []

while capacity_of_cups and bottle_capacity:
    bottle = bottle_capacity.pop()
    cups = capacity_of_cups.popleft()
    if cups - bottle <= 0:
        result = bottle - cups
        water_left.append(result)
    elif cups - bottle > 0:
        while cups > 0:
            cups -= bottle
            if cups > 0:
                bottle = bottle_capacity.pop()
            else:
                water_left.append(abs(cups))
if not capacity_of_cups:
    if bottle_capacity:
        print(f'Bottles: {" ".join([str(bottle_capacity[i]) for i in range(len(bottle_capacity)-1, -1, -1)])}')
    else:
        print(f'Bottles: 0')
if not bottle_capacity:
    if capacity_of_cups:
        print(f'Cups: {" ".join([str(i) for i in capacity_of_cups])}')
    else:
        print(f'Cups: 0')
print(f'Wasted litters of water: {sum(water_left)}')