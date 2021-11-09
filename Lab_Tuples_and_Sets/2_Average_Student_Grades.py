num = int(input())

students = {}
for i in range(num):
    name, grate = input().split()
    if name not in students: students[name] = []
    students[name].append(float(grate))

for k, v in students.items():
    print(f"{k} -> {' '.join(tuple([f'{i:.2f}' for i in v]))} (avg: {sum(v) / len(v):.2f})")