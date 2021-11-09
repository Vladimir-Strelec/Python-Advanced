n = int(input())

unique_element = set([])
for _ in range(n):
    x = [i for i in input().split()]
    for i in x:
        unique_element.add(i)

print('\n'.join(unique_element))