neighborhood_data = [int(s) for s in input().split('@')]
command = input()
current_position = 0

while command != 'Love!':
    command, value = command.split()
    value = int(value)
    if current_position + value < len(neighborhood_data):
        current_position += value
    else:
        current_position = 0
    neighborhood_data[current_position] -= 2
    if neighborhood_data[current_position] == 0:
        print(f'Place {current_position} has Valentine\'s day.')
    elif neighborhood_data[current_position] < 0:
        print(f'Place {current_position} already had Valentine\'s day.')

    command = input()

count_not_valentine = sum(map(lambda x: x != 0 and x > 0, neighborhood_data))
print(f'Cupid\'s last position was {current_position}.')
if count_not_valentine > 0:
    print(f'Cupid has failed {count_not_valentine} places.')
else:
    print(f'Mission was successful.')