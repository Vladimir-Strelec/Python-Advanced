def numbers_searching(*args):
    sort = sorted(args)
    set_nums = sorted(set([int(el) for el in sort if sort.count(int(el)) > 1]))
    exscluzive = []
    matrix = []
    num_min, num_max = min(sort), max(sort)
    for index in range(num_min, num_max+1):
        if index not in sort:
            exscluzive.append(index)
    for _ in range(len(exscluzive)):
        matrix.append(*[int(i) for i in exscluzive])
        matrix.append(set_nums)
    return matrix



print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))