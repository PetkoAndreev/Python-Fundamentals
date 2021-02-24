gifts_data = input().split()
command = input()

while command != 'No Money':
    command = command.split()
    if command[0] == 'OutOfStock':
        for index in range(len(gifts_data)):
            if gifts_data[index] == command[1]:
                gifts_data[index] = 'None'

    elif command[0] == 'Required':
        if 0 <= int(command[2]) < (len(gifts_data)):
            gifts_data[int(command[2])] = command[1]

    elif command[0] == 'JustInCase':
        gifts_data[-1] = command[1]
    command = input()

print(' '.join([i for i in gifts_data if i != 'None']))