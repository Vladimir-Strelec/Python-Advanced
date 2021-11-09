# a = set([33, 44, 55])
# b = set([30, 44, 50])
#
# print(a.symmetric_difference(b))
n = int(input())
num_guest = set()
guest = set()

for _ in range(n):
    num_guest.add(input())

command = input()
while not command == "END":
    guest.add(command)
    command = input()

print(len(num_guest.difference(guest)))
print('\n'.join(sorted(num_guest.difference(guest))))