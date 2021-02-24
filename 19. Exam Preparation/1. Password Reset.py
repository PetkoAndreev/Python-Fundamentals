raw_password = input()
command_data = input()

while command_data != 'Done':
    command_list = command_data.split()
    command = command_list[0]

    if command == 'TakeOdd':
        new_raw_password = ''
        for i in range(len(raw_password)):
            if i % 2 != 0:
                new_raw_password += raw_password[i]
        raw_password = new_raw_password
        print(raw_password)

    elif command == 'Cut':
        index = int(command_list[1])
        length = int(command_list[2])
        raw_password = raw_password[:index] + raw_password[(index + length):]
        print(raw_password)

    elif command == 'Substitute':
        substring = command_list[1]
        substitute = command_list[2]
        if raw_password.count(substring) > 0:
            while raw_password.count(substring) > 0:
                raw_password = raw_password.replace(substring, substitute)
            print(raw_password)
        else:
            print('Nothing to replace!')

    command_data = input()

print(f'Your password is: {raw_password}')