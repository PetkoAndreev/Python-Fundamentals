def password_validator(password):
    digit_counter = 0
    letter_counter = 0
    special_counter = 0
    result = []
    for symbol in password:
        if ord(symbol) in range(48, 58):
           digit_counter += 1
        elif ord(symbol) in range(65, 91) or ord(symbol) in range(97, 123):
            letter_counter += 1
        else:
            special_counter += 1
    if digit_counter + letter_counter + special_counter in range(6, 11) and digit_counter >= 2 and special_counter == 0:
        result.append('Password is valid')
    if digit_counter + letter_counter + special_counter not in range(6, 11):
        result.append('Password must be between 6 and 10 characters')
    if special_counter > 0:
        result.append('Password must consist only of letters and digits')
    if digit_counter < 2:
        result.append('Password must have at least 2 digits')

    return '\n'.join(result)

pass_value = input()
print(password_validator(pass_value))