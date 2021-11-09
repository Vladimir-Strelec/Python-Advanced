def generate_sequence(n):
    lin_num = [0, 1]
    for i in range(2, n):
        lin_num.append(lin_num[-1] + lin_num[-2])
    return lin_num


def dinf_number(num, line):
    if num in line:
        return print(f"The number - {num} is at index {line.index(num)}")
    return print(f"The number {num} is not in the sequence")