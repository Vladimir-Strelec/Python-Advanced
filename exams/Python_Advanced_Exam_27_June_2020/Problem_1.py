from collections import deque

line_firework_effect = deque(list(map(int, input().split(', '))))
line_explosive_casings = deque(list(map(int, input().split(', '))))

line_dict = {40: 'Datura Bombs', 60: 'Cherry Bombs', 120: 'Smoke Decoy Bombs'}
result_dict = {'Datura Bombs': 0, 'Cherry Bombs': 0, 'Smoke Decoy Bombs': 0}
x = False
while line_firework_effect and line_explosive_casings:
    current_effect = line_firework_effect.popleft()
    current_casings = line_explosive_casings.pop()

    if (current_casings + current_effect) in line_dict:
        current_key = (current_casings + current_effect)
        result_dict[line_dict[current_key]] += 1

    else:
        line_firework_effect.appendleft(current_effect)
        if (current_casings - 5) >= 0:
            line_explosive_casings.append(current_casings - 5)
    if result_dict['Datura Bombs'] >= 3 and result_dict['Cherry Bombs'] >= 3 and result_dict['Smoke Decoy Bombs'] >= 3:
        print(f"Bene! You have successfully filled the bomb pouch!")
        x = True
        break

filter_dict = sorted(result_dict.items())

if not x:
    print("You don't have enough materials to fill the bomb pouch.")
if line_firework_effect: print(f"Bomb Effects: {', '.join([str(i) for i in line_firework_effect])}", sep=', ')
else:
    print('Bomb Effects: empty')

if line_explosive_casings: print(f"Bomb Casings: {', '.join([str(i) for i in line_explosive_casings])}", sep=', ')
else:
    print('Bomb Casings: empty')

print('\n'.join([f"{k}: {v}" for k, v in filter_dict]))