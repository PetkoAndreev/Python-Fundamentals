elements = input().split()
command = input()
moves = 0

while command != 'end':
    moves += 1
    i_1, i_2 = command.split()
    i_1 = int(i_1)
    i_2 = int(i_2)
    if len(elements) == 0:
        moves -= 1
    elif i_1 not in range(0, len(elements)) or i_2 not in range(0, len(elements)) or i_1 == i_2:
        print('Invalid input! Adding additional elements to the board')
        elements.insert((len(elements)) // 2, str(-moves) + 'a')
        elements.insert((len(elements)) // 2, str(-moves) + 'a')
    elif elements[i_1] == elements[i_2]:
        print(f'Congrats! You have found matching elements - {elements[i_1]}!')
        value_to_remove = elements[i_1]
        elements.remove(value_to_remove)
        elements.remove(value_to_remove)
    elif elements[i_1] != elements[i_2]:
        print('Try again!')
    command = input()

if len(elements) == 0:
    print(f'You have won in {moves} turns!')
else:
    print('Sorry you lose :(\n'
          f'{" ".join(elements)}')