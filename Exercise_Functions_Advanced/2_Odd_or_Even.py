def odd_or_even(com, nums):
    result = []
    if com == 'Even':
        return list(filter(lambda x: x % 2 == 0, nums))
    return list(filter(lambda x: x % 2 != 0, nums))


command = input()
numbers = list(map(int, input().split()))
print(sum(odd_or_even(command, numbers)*len(numbers)))
