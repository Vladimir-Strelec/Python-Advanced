from collections import deque
line_name = input()

result = deque([])
while not line_name == "End":
    result.append(line_name)
    line_name = input()
while "Paid" in result:
    while result:
        chek = result.popleft()
        if not chek == "Paid":
            print(chek)
            continue
        break
print(f"{len(result)} people remaining.")