from collections import deque


def best_list_pureness(numbers, k):
    numbers = deque(numbers)
    data = {}
    for i in range(k+1):
        result = sum([index*number for index, number in enumerate(numbers)])
        data.update({i: result})
        numbers.rotate()
    max_value = max(data.values())
    for k, v in data.items():
        if v == max_value:
            return f"Best pureness {max_value} after {k} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)
test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)


