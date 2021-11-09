def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


def func_executor(*args):
    list_result = []
    for func_name, data in args:
        list_result.append(func_name(*data))
    return list_result


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))