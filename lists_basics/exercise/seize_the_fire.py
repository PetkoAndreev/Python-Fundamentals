fire_data = input().split('#')
water = int(input())
result_list = []
total_fire = 0
effort = 0

for fire in fire_data:
    fire_type, fire_value = fire.split(' = ')
    fire_value = int(fire_value)

    if fire_type == 'Low' and fire_value not in range(1, 51):
        continue
    elif fire_type == 'Medium' and fire_value not in range(51, 81):
        continue
    elif fire_type == 'High' and fire_value not in range(81, 126):
        continue

    if water >= fire_value:
        total_fire += fire_value
        effort += 0.25 * fire_value
        water -= fire_value
        result_list.append(fire_value)

print('Cells:')
for fire_value in result_list:
    print(f" - {fire_value}")
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')