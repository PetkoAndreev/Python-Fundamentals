encrypt_message = input()
data = input()

while data != 'Decode':
    data = data.split('|')
    command = data[0]

    if command == 'Move':
        num_letters = int(data[1])
        encrypt_message = encrypt_message[num_letters:] + encrypt_message[:num_letters]

    elif command == 'Insert':
        index = int(data[1])
        value = data[2]
        encrypt_message = encrypt_message[:index] + value + encrypt_message[index:]

    elif command == 'ChangeAll':
        substring = data[1]
        replacement = data[2]
        encrypt_message = encrypt_message.replace(substring, replacement)

    data = input()

print(f'The decrypted message is: {encrypt_message}')