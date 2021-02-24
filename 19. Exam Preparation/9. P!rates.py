city_input = input()
cities = {}

while city_input != 'Sail':
    city, population, gold = city_input.split('||')
    population = int(population)
    gold = int(gold)
    if city in cities:
        cities[city][0] += population
        cities[city][1] += gold
    else:
        cities[city] = [population, gold]
    city_input = input()

action_input = input()

while action_input != 'End':
    action_input = action_input.split('=>')
    action = action_input[0]
    city = action_input[1]
    if action == 'Plunder':
        people = int(action_input[2])
        gold = int(action_input[3])
        city_population = cities[city][0]
        city_treasury = cities[city][1]
        print(f'{city} plundered! {gold} gold stolen, {people} citizens killed.')
        if city_population - people <= 0 or city_treasury - gold <= 0:
            print(f'{city} has been wiped off the map!')
            del cities[city]
        else:
            cities[city][0] = city_population - people
            cities[city][1] = city_treasury - gold

    elif action == 'Prosper':
        gold = int(action_input[2])
        if gold < 0:
            print('Gold added cannot be a negative number!')
        else:
            city_treasury = cities[city][1] + gold
            cities[city][1] = city_treasury
            print(f'{gold} gold added to the city treasury. {city} now has {city_treasury} gold.')

    action_input = input()

cities = dict(sorted(cities.items(), key=lambda s: (-s[1][1], s[0])))

if cities == {}:
    print('Ahoy, Captain! All targets have been plundered and destroyed!')
else:
    print(f'Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:')
    for city, value in cities.items():
        print(f'{city} -> Population: {value[0]} citizens, Gold: {value[1]} kg')