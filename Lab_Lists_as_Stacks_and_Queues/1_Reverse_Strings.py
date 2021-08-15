# line_text = list(input())
# while line_text:
#     print(line_text.pop(), end="")
# exit()
text = list(input())
print("".join([text.pop() for i in range(len(text))]))