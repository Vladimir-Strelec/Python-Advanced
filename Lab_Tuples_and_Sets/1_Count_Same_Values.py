line_text = tuple([float(i) for i in input().split()])
line_dict = {i: line_text.count(i) for i in line_text}

print('\n'.join([f"{k} - {v} times" for k, v in line_dict.items()]))