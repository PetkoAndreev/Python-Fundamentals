message = input()
command_data = input()

while command_data != 'Reveal':
    command_data = command_data.split(':|:')
    command = command_data[0]

    if command == 'InsertSpace':
        index = int(command_data[1])
        message = message[:index] + ' ' + message[index:]
        print(message)

    elif command == 'Reverse':
        substring = command_data[1]
        if substring in message:
            message = message.replace(substring, '', 1)
            substring = substring[-1::-1]
            message = message + substring
            print(message)
        else:
            print('error')

    elif command == 'ChangeAll':
        substring = command_data[1]
        replacement = command_data[2]
        while message.count(substring) > 0:
            message = message.replace(substring, replacement)
        print(message)

    command_data = input()

print(f'You have a new text message: {message}')