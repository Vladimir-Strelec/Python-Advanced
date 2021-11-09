from collections import deque

line_firework_effect = deque(list(map(int, input().split(', '))))
line_explosive_power = deque(list(map(int, input().split(', '))))

line_dict = {'Palm': 0, 'Willow': 0, 'Crossette': 0}
while line_firework_effect and line_explosive_power:
    current_effect = line_firework_effect.popleft()
    current_power = line_explosive_power.pop()
    if current_power <= 0 or current_effect <= 0:
        if current_effect <= 0 and current_power > 0:
            line_explosive_power.append(current_power)

        elif current_effect > 0 and current_power <= 0:
            line_firework_effect.appendleft(current_effect)

        continue
    if (current_effect + current_power) % 3 == 0 and (current_effect + current_power) % 5 == 0:
        line_dict['Crossette'] += 1
    elif (current_effect + current_power) % 3 == 0:
        line_dict['Palm'] += 1
    elif (current_effect + current_power) % 5 == 0:
        line_dict['Willow'] += 1

    else:
        line_firework_effect.append(current_effect - 1)
        line_explosive_power.append(current_power)
    if line_dict['Palm'] >= 3 and line_dict['Willow'] >= 3 and line_dict['Crossette'] >= 3:
        break
if line_dict['Palm'] >= 3 and line_dict['Willow'] >= 3 and line_dict['Crossette'] >= 3:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if line_firework_effect:
    print(f"Firework Effects left: {', '.join([str(i) for i in line_firework_effect])}")
if line_explosive_power:
    print(f"Explosive Power left: {', '.join(list(map(str, line_explosive_power)))}")

print(f"Palm Fireworks: {line_dict['Palm']}")
print(f"Willow Fireworks: {line_dict['Willow']}")
print(f"Crossette Fireworks: {line_dict['Crossette']}")