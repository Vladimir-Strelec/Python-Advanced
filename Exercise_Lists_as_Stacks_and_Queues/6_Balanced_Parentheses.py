line_paren = input()
check = True
stack = []

for i in line_paren:
    if i in "([{":
        stack.append(i)
        continue
    elif i in ")]}":
        if len(stack) == 0:
            check = False
            break
        opening_paren = stack.pop()

        if f'{opening_paren}{i}' not in ['()', '[]', '{}']:
            check = False
            break
if check and len(stack) == 0:
    print('YES')
else:
    print('NO')
