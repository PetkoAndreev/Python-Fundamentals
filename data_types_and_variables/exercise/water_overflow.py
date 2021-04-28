liter_lines = int(input())
tank_capacity = 255

while liter_lines > 0:
    current_liter_line = int(input())
    if tank_capacity - current_liter_line < 0:
        print('Insufficient capacity!')
    else:
        tank_capacity -= current_liter_line
    liter_lines -= 1

print(255 - tank_capacity)