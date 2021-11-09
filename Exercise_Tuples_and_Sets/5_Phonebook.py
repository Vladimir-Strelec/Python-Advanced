name_and_number = input()

line_data = set([])
while not name_and_number.isdigit():
    line_data.add(name_and_number)
    name_and_number = input()
for i in range(int(name_and_number)):
    name = input()
    change_contact = [j for j in line_data if name in j]
    if change_contact:
        print(''.join(change_contact))
    else:
        print(f"Contact {name} does not exist.")
    change_contact = []
