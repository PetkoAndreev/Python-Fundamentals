data_to_encrypt = input()
encrypted_data = []

for el in data_to_encrypt:
    encrypted_data .append(chr(ord(el) + 3))

print(''.join(encrypted_data))