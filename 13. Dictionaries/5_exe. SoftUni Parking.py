num_commands = int(input())
parking_data = {}

for i in range(1, num_commands + 1):
    command = input().split()
    action = command[0]
    if action == 'register':
        user = command[1]
        license_plate = command[2]
        if user in parking_data:
            print(f'ERROR: already registered with plate number {parking_data[user]}')
        else:
            parking_data[user] = license_plate
            print(f'{user} registered {license_plate} successfully')
    elif action == 'unregister':
        user = command[1]
        if user not in parking_data:
            print(f'ERROR: user {user} not found')
        else:
            print(f'{user} unregistered successfully')
            parking_data.pop(user)

for user, license_plate in parking_data.items():
    print(f'{user} => {license_plate}')