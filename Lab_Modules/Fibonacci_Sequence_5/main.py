from Python_Advanced.Lab_Modules.Fibonacci_Sequence_5.helper import *

while True:
    command = input()
    if command == "Stop":
        break

    command = command.split()
    if command[0] == "Create":
        line = generate_sequence(int(command[2]))
        print(*line, sep=" ")
    elif command[0] == "Locate":
        dinf_number(int(command[1]), line)
