numbers = [int(s) for s in input().split()]

command = input()

while command != 'end':
    command = command.split()
    action = command[0]
    if action == 'swap':
        index_1 = int(command[1])
        index_2 = int(command[2])
        numbers[index_1], numbers[index_2] = numbers[index_2], numbers[index_1]
    elif action == 'multiply':
        index_1 = int(command[1])
        index_2 = int(command[2])
        numbers[index_1] = numbers[index_1] * numbers[index_2]
    elif action == 'decrease':
        numbers = [s - 1 for s in numbers]

    command = input()

numbers = [str(s) for s in numbers]
print(', '.join(numbers))