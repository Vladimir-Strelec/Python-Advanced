def list_manipulator(list_nums, command, direction, *args):
    if command == 'add':
        if direction == 'end':
            a = args
            return list_nums + list(args)
        elif direction == 'beginning':
            return list(args) + list_nums
    elif command == 'remove':
        if direction == 'end':
            if args:
                a = args
                for _ in range(*args):
                    list_nums.pop()
                return list_nums
            list_nums.pop()
            return list_nums
        elif direction == 'beginning':
            if args:
                return list_nums[args[0]:]
            return list_nums[1:]


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning", ))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))