# def loop(index, max_index):
#     if index == max_index:
#         print(f" -- ending loop({index}, {max_index})--")
#         return
#     print(f' -- starting loop ({index}, {max_index})--')
#     print(index)
#     loop(index=index+1, max_index=max_index)
#
#     print(f" -- ending loop({index}, {max_index})--")
#
#
# loop(0, 10)

def combo(text, index=0):
    if len(text) == index:
        print(''.join(text))
        return

    for i in range(index, len(text)):
        text[index], text[i] = text[i], text[index]
        combo(text, index + 1)
        text[index], text[i] = text[i], text[index]


line_text = list(map(str, input()))
combo(line_text)