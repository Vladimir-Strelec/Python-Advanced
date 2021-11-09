line_sep = [int(i) for i in input().split()]

line_1 = set([input() for _ in range(line_sep[0])])
line_2 = set([input() for _ in range(line_sep[1])])

print("\n".join(line_1.intersection(line_2)))