from functools import reduce
# print(list(map(lambda x: abs(float(x)), input().split())))


def multiply(*args):
    return reduce((lambda x, a: x*a), args)


print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))