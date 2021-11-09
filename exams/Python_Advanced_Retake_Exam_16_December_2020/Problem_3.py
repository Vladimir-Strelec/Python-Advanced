# def get_magic_triangle(n):
#     triangle = [[1], [1, 1]]
#     for i in range(2, n):
#         triangle.append([])
#         triangle[-1].append(1)
#         for j in range(1, i):
#             triangle[-1].append(triangle[i - 1][j-1]+triangle[i-1][j])
#         triangle[-1].append(1)
#     return triangle

def get_magic_triangle(n):
    matrix = []
    for i in range(n):
        matrix.append([1])
        for j in range(1, i):
            matrix[-1].append(matrix[i-1][j-1] + matrix[i-1][j])
        if i != 0:
            matrix[-1].append(1)
    return matrix


print(get_magic_triangle(5))