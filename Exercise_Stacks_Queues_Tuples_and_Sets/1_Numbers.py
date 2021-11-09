line_first = set([int(i) for i in input().split()])
line_second = set([int(i) for i in input().split()])
n = int(input())

for _ in range(n):
    command = input().split()
    if command[0] == "Add":
        if command[1] == "First":
            line_first = line_first.union([int(i) for i in command[2:]])
        else:
            line_second = line_second.union([int(i) for i in command[2:]])
    elif command[0] == "Remove":
        if command[1] == "First":
            [line_first.discard(int(i)) for i in command[2:]]
        else:
            [line_second.discard(int(i)) for i in command[2:]]
    else:
        if line_first.issubset(line_second) or line_first.issuperset(line_second):
            print('True')
        else:
            print('False')
print(', '.join(list(map(str, sorted(line_first)))))
print(', '.join(list(map(str, sorted(line_second)))))
