bread_data = input().split('|')
current_energy = 100
current_coins = 100
is_bankrupt = False

for bread in bread_data:
    event, value = bread.split('-')
    value = int(value)
    if event == 'rest':
        if current_energy + value <= 100:
            current_energy += value
        else:
            value = 0

        print(f'You gained {value} energy.')
        print(f'Current energy: {current_energy}.')

    elif event == 'order':
        if current_energy >= 30:
            current_energy -= 30
            current_coins += value
            print(f'You earned {value} coins.')
        else:
            current_energy += 50
            print('You had to rest!')

    elif current_coins >= 0 and current_coins > value:
        current_coins -= value
        print(f'You bought {event}.')

    else:
        print(f'Closed! Cannot afford {event}.')
        is_bankrupt = True
        break

if not is_bankrupt:
    print('Day completed!')
    print(f'Coins: {current_coins}')
    print(f'Energy: {current_energy}')