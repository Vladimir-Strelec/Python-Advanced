from collections import deque

price_bullet = int(input())
size_gun_barrel = int(input()) #Baraban
sequence_bullet = deque(map(int, input().split())) #kol patronov
line_locks = deque(map(int, input().split()))  #kol zamkov
value_the_intelligence = int(input())

count_shooting = 0
reload = size_gun_barrel
while sequence_bullet and line_locks:
    count_shooting += 1
    reload -= 1
    bullet = sequence_bullet.pop()
    locks = line_locks.popleft()
    if bullet <= locks: print('Bang!')
    elif bullet > locks:
        line_locks.appendleft(locks)
        print(f'Ping!')
    if reload == 0 and len(sequence_bullet):
        print('Reloading!')
        reload = size_gun_barrel

if len(sequence_bullet) >= len(line_locks):
    print(f"{len(sequence_bullet)} bullets left. Earned ${value_the_intelligence - count_shooting * price_bullet}")
elif len(sequence_bullet) < len(line_locks):
    print(f"Couldn't get through. Locks left: {len(line_locks)}")
else:
    print(f"{len(sequence_bullet)} bullets left. Earned ${value_the_intelligence - count_shooting * price_bullet}")