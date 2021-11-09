line_items = input().split()
line_items = list(map(int, line_items))
quantity = int(input())

chek = 0
count_clothes = 0
while line_items:
    if chek + line_items[-1] <= quantity:
        chek += line_items.pop()
    else:
        chek = 0
        count_clothes += 1

if chek > 0 and chek <= quantity:
    count_clothes += 1
print(count_clothes)