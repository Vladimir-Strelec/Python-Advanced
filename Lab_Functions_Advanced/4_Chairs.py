def names(num, name, current_name=[]):
    if len(current_name) == num:
        print(', '.join(current_name))
        return

    for i in range(len(name)):
        current_name.append(name[i])
        names(num, name[i+1:], current_name)
        current_name.pop()


line_name = input().split(', ')
n = int(input())
names(n, line_name)