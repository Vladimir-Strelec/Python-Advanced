from constants import *
num1, operatror, num_2 = input().split()
num1, num_2 = int(num1), int(num_2)

try:
    print(mapper[operatror](num1, num_2))
except KeyError:
    print("Invalid operation")