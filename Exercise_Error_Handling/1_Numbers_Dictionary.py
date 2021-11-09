numbers_dictionary = {}


line = input()
while not line == 'End':
    if line != "Search" and line != "Remove":
        try:
            number = int(input())
            numbers_dictionary[line] = number
        except ValueError:
            print('The variable number must be an integer')
            break
    elif line == 'Search':
        key = input()
        try:
            print(numbers_dictionary[key])

        except KeyError:
            print("Number does not exist in dictionary")
            break
    elif line == 'Remove':
        key = input()
        try:
            del numbers_dictionary[key]
        except KeyError:
            print("Number does not exist in dictionary")
            break
    line = input()

print(numbers_dictionary)
