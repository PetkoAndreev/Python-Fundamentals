destinations = input()
command_data = input()

while command_data != 'Travel':
    command_data = command_data.split(':')
    command = command_data[0]

    if command == 'Add Stop':
        index = int(command_data[1])
        string = command_data[2]
        if index in range(0, len(destinations)):
            destinations = destinations[:index] + string + destinations[index:]
        print(destinations)

    elif command == 'Remove Stop':
        start_index = int(command_data[1])
        end_index = int(command_data[2])
        if start_index in range(0, len(destinations)) and end_index in range(0, len(destinations)):
            destinations = destinations[:start_index] + destinations[end_index+1:]
        print(destinations)

    elif command == 'Switch':
        old_string = command_data[1]
        new_string = command_data[2]
        if old_string in destinations:
            destinations = destinations.replace(old_string, new_string)
        print(destinations)
    command_data = input()
print(f'Ready for world tour! Planned stops: {destinations}')