activation_key = input()
data = input()

while data != 'Generate':
    data = data.split('>>>')
    command = data[0]
    if command == 'Contains':
        substr_to_check = data[1]
        if substr_to_check in activation_key:
            print(f'{activation_key} contains {substr_to_check}')
        else:
            print('Substring not found!')

    elif command == 'Flip':
        action = data[1]
        start_index = int(data[2])
        end_index = int(data[3])
        for i in range(start_index, end_index):
            if action == 'Upper':
                activation_key = activation_key[:i] + activation_key[i].upper() + activation_key[i+1:]
            elif action == 'Lower':
                activation_key = activation_key[:i] + activation_key[i].lower() + activation_key[i+1:]
        print(activation_key)

    elif command == 'Slice':
        start_index = int(data[1])
        end_index = int(data[2])
        activation_key = activation_key[0:start_index] + activation_key[end_index:len(activation_key)]
        print(activation_key)

    data = input()

print(f'Your activation key is: {activation_key}')