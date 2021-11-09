from collections import deque
boxes = [int(i) for i in input().split()]
magic_value = deque([int(i) for i in input().split()])

presents = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle',
}

crafted = {}

while boxes and magic_value:
    box = boxes.pop()
    magic = magic_value.popleft()
    result = box * magic

    if box == 0 and magic == 0:
        continue
    if box == 0:
        magic_value.appendleft(magic)
        continue
    if magic == 0:
        boxes.append(box)
        continue

    if result < 0:
        boxes.append(box + magic)

    elif result in presents:
        present = presents[result]
        if present in crafted:
            crafted[present] += 1
        else:
            crafted[present] = 1
    else:
        boxes.append(box + 15)
is_done = ('Doll' in crafted and 'Wooden train' in crafted) or \
          ('Teddy bear' in crafted and 'Bicycle' in crafted)

if is_done:
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')

if boxes:
    print(f"Materials left: {', '.join(reversed(list(map(str, boxes))))}")
if magic_value:
    print(f"Magic left: {', '.join(list(map(str, magic_value)))}")

for k, v in sorted(crafted.items()):
    print(f'{k}: {v}')