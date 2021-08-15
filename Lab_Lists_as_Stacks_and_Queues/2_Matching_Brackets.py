# line_text = list(input())
# stack = []
#
# for i in line_text:
#     if i == "(":
#         stack.append('')
#
#     for index in range(len(stack)):
#         stack[index] += i
#
#     if i == ")":
#         print(f'{stack.pop()}')

line_text = input()
stack = []
for i, chr in enumerate(line_text):
    if chr == '(':
        stack.append(i)
    elif chr == ')':
        end_index = i
        start_index = stack.pop()
        print(line_text[start_index: end_index + 1])