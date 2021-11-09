def change_cr_in_int(a, b):
    result = [i for i in range(a, b + 1)]
    return result


n = int(input())
result_intersection = set([])

for _ in range(n):

    first, second = input().split('-')
    first_start, first_end = [int(i) for i in first.split(',')]
    second_start, second_end = [int(i) for i in second.split(',')]

    result_first = change_cr_in_int(int(first_start), int(first_end))
    result_second = change_cr_in_int(int(second_start), int(second_end))

    intersection = set(result_first).intersection(result_second)
    if len(intersection) > len(result_intersection):
        result_intersection = intersection

print(f"Longest intersection is {[i for i in result_intersection]} with length {len(result_intersection)}")