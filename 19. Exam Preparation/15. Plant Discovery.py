num_plants = int(input())
plants = {}

for i in range(1, num_plants+1):
    plant, rarity = input().split('<->')
    rarity = int(rarity)
    plants[plant] = [rarity]

command_data = input()

while command_data != 'Exhibition':
    command_data = command_data.split(': ')
    command = command_data[0]
    if command == 'Rate':
        plant, rating = command_data[1].split(' - ')
        rating = float(rating)
        if plant in plants:
            plants[plant].append(rating)
        else:
            print('error')

    elif command == 'Update':
        plant, new_rarity = command_data[1].split(' - ')
        new_rarity = int(new_rarity)
        if plant in plants:
            plants[plant][0] = new_rarity
        else:
            print('error')

    elif command == 'Reset':
        plant = command_data[1]
        if plant in plants:
            plants[plant] = [plants[plant][0]]
        else:
            print('error')

    command_data = input()

plants_result = {}

for plant, value in plants.items():
    rarity = value[0]
    if len(value) > 1:
        average_rating = sum(value[1:])/(len(value)-1)
    else:
        average_rating = 0
    plants_result[plant] = [rarity, average_rating]

plants_result = dict(sorted(plants_result.items(), key=lambda s: (-s[1][0], -s[1][1])))

print('Plants for the exhibition:')
for plant, value in plants_result.items():
    rarity = value[0]
    average_rating = value[1]
    print(f'- {plant}; Rarity: {rarity}; Rating: {average_rating:.2f}')