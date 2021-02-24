numbers = [int(s) for s in input().split('.')]

if numbers[2] == 9:
    numbers[2] = 0
    if int(numbers[1]) == 9:
        numbers[1] = 0
        numbers[0] = numbers[0] + 1
    else:
        numbers[1] = numbers[1] + 1
else:
    numbers[2] = numbers[2] + 1

numbers = [str(s) for s in numbers]

print('.'.join(numbers))