def get_range(s, row, col):
    if 0 <= row < s and 0 <= col < s:
        return True
    return False


size = 5
matrix = []
position_target = []
count_target = 0
player_row, player_col = 0, 0
for i in range(size):
    element = input().split()
    matrix.append(element)
    for j in range(len(element)):
        if element[j] == "A":
            player_row, player_col = i, j
        elif element[j] == "x":
            count_target += 1
count_commands = int(input())

move_dict = {
    "up": lambda r, c: (r-step, c),
    "down": lambda r, c: (r+step, c),
    "left": lambda r, c: (r, c-step),
    "right": lambda r, c: (r, c+step)
}

for _ in range(count_commands):
    command = input().split()
    if command[0] == "shoot":
        step = 1
        position_shooting_row, position_shooting_col = player_row, player_col
        while True:
            position_shooting_row, position_shooting_col = move_dict[command[1]](position_shooting_row, position_shooting_col)
            if not get_range(size, position_shooting_row, position_shooting_col):
                break
            if matrix[position_shooting_row][position_shooting_col] == "x":
                position_target.append([position_shooting_row, position_shooting_col])
                count_target -= 1
                matrix[position_shooting_row][position_shooting_col] = "."
                break

    elif command[0] == "move":
        step = int(command[2])
        new_pos_player_row, new_pos_player_col = move_dict[command[1]](player_row, player_col)
        if not get_range(size, new_pos_player_row, new_pos_player_col):
            continue
        if matrix[new_pos_player_row][new_pos_player_col] != ".":
            continue
        matrix[new_pos_player_row][new_pos_player_col] = "A"
        matrix[player_row][player_col] = "."
        player_row, player_col = new_pos_player_row, new_pos_player_col

    if count_target == 0:
        break
if count_target == 0:
    print(f"Training completed! All {len(position_target)} targets hit.")
elif count_target > 0:
    print(f"Training not completed! {count_target} targets left.")
for i in range(len(position_target)):
    print(position_target[i])