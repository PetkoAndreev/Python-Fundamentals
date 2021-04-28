targets_data = [int(s) for s in input().split()]
command = input()

while command != 'End':
    command, index, value = command.split()
    index = int(index)
    value = int(value)
    if command == 'Shoot':
        if len(targets_data) > index >= 0:
            targets_data[index] -= value
            if targets_data[index] <= 0:
                targets_data.pop(index)

    elif command == 'Add':
        if len(targets_data) > index >= 0:
            targets_data.insert(index, value)
        else:
            print('Invalid placement!')

    elif command == 'Strike':
        if index + value < len(targets_data) and index - value >= 0:
            counter = (value * 2) + 1
            while counter > 0:
                targets_data.pop(index - value)
                counter -= 1
        else:
            print('Strike missed!')

    command = input()
targets_data = [str(s) for s in targets_data]
print('|'.join(targets_data))