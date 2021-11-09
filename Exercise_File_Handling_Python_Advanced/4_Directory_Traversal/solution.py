import os


def count_directories(dir_path, result):
    for x in os.listdir(dir_path):
        file_with_path = os.path.join(dir_path, x)
        if os.path.isfile(os.path.join(dir_path, x)):
            ext = x.split('.')[-1]
            if ext not in result:
                result[ext] = []
            result[ext].append(file_with_path)

        elif os.path.isdir(os.path.join(file_with_path, x)):
            count_directories(file_with_path, result)


result = {}
count_directories(os.getcwd(), result)

with open("output.txt", 'w') as result_file:
    for k, v in sorted(result.items()):
        result_file.write(f'.{k}')
        result_file.write('\n')
        for value in sorted(v):
            result_file.write(f"---{value}")
            result_file.write(f"\n")