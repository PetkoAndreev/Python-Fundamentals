num_cars = int(input())
cars = {}
for i in range(1, num_cars + 1):
    car_detail = input()
    car, mileage, fuel = car_detail.split('|')
    mileage = int(mileage)
    fuel = int(fuel)
    if car in cars:
        cars[car][0] += mileage
        cars[car][1] += fuel
    else:
        cars[car] = [mileage, fuel]

command_data = input()


def drive(car, distance, fuel):
    if fuel > cars[car][1]:
        print('Not enough fuel to make that ride')
    else:
        cars[car][0] += distance
        cars[car][1] -= fuel
        print(f'{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.')
        if cars[car][0] >= 100000:
            print(f'Time to sell the {car}!')
            del cars[car]
    return cars


def refuel(car, fuel):
    if cars[car][1] + fuel > 75:
        print(f'{car} refueled with {75 - cars[car][1]} liters')
        cars[car][1] = 75
    else:
        cars[car][1] += fuel
        print(f'{car} refueled with {fuel} liters')
    return cars


def revert(car, kilometers):
    if cars[car][0] - kilometers < 10000:
        cars[car][0] = 10000
    else:
        cars[car][0] -= kilometers
        print(f'{car} mileage decreased by {kilometers} kilometers')

    return cars


while command_data != 'Stop':
    command_data = command_data.split(' : ')
    command = command_data[0]

    if command == 'Drive':
        car = command_data[1]
        distance = int(command_data[2])
        fuel = int(command_data[3])
        drive(car, distance, fuel)

    elif command == 'Refuel':
        car = command_data[1]
        fuel = int(command_data[2])
        refuel(car, fuel)

    elif command == 'Revert':
        car = command_data[1]
        kilometers = int(command_data[2])
        revert(car, kilometers)

    command_data = input()

cars = dict(sorted(cars.items(), key=lambda s: (-s[1][0], s[0])))

for car, value in cars.items():
    mileage = value[0]
    fuel = value[1]
    print(f'{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.')
