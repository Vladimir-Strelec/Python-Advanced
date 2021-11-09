line_num = input().split('|')
result = []

for i in line_num:
    result.append(i.split())

for i in range(len(result)-1, -1, -1):
    for j in result[i]:
        print(''.join(j), end=' ')
