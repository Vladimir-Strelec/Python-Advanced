man_line = [int(el) for el in input().split() if int(el) > 0]
girl_line = [int(el) for el in input().split() if int(el) > 0]
match = 0
i = 0
while i < len(man_line) and i < len(girl_line):
    if man_line[-1] % 25 == 0:
        del man_line[:-3:-1]
    if man_line[-1] == girl_line[i]:
        match += 1
        man_line.pop()
        girl_line.reverse()
        girl_line.pop()
        girl_line.reverse()
    else:
        man_line[-1] -= 2
        if man_line[-1] <= 0:
            man_line.pop()
        girl_line.reverse()
        girl_line.pop()
        girl_line.reverse()

print(f"Matches: {match}")
if len(man_line) > 0:
    print(f"Males left: {', '.join([str(man_line[i]) for i in range(len(man_line)-1, -1, -1)])}")
else:
    print("Males left: none")

if len(girl_line) > 0:
    print(f"Females left: {', '.join([str(girl_line[i]) for i in range(len(girl_line))])}")
else:
    print(f"Females left: none")