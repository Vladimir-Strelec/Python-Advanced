def first(n):

    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()


def second(n):

    for i in range(n, 0, -1):
        for j in range(1, i):
            print(j, end=" ")
        print()


def print_first_second_func(n):
    first(n)
    second(n)