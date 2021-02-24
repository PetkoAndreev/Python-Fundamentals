input_year = int(input())
input_year += 1

while True:
    if len(str(input_year)) <= len(set(str(input_year))):
        break
    else:
        input_year += 1

print(f'{input_year}')