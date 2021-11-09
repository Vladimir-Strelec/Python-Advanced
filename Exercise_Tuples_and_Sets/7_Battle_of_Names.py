n = int(input())

even = set([])
odd = set([])
for i in range(1, n + 1):
    name = [ord(j) for j in input()]
    num = int(sum(name) / i)
    if num % 2 == 0:
        even.add(num)
    else:
        odd.add(num)
if sum(even) > sum(odd):
    print(', '.join([str(n) for n in even.symmetric_difference(odd)]))
else:
    print(', '.join([str(n) for n in odd.difference(even)]))
