import sys

data_to_manipulate = input().split()
command = input()

while command != 'end':
    # Here we split the command 2 or 3 variables, depends on the command.
    if 'first' in command or 'last' in command:
        command, index, type_num = command.split()
    else:
        command, index = command.split()
    # Conditions for the Exchange command
    if command == 'exchange':
        index = int(index)
        result_exchange = []
        if index >= len(data_to_manipulate) or index < 0:
            print('Invalid index')
        else:
            for first_half in range(len(data_to_manipulate)):
                if first_half > index:
                    result_exchange.append(data_to_manipulate[first_half])

            for second_half in range(len(data_to_manipulate)):
                if second_half <= index:
                    result_exchange.append(data_to_manipulate[second_half])
                else:
                    break
            data_to_manipulate = result_exchange
            result_exchange = ', '.join(result_exchange)

    # Conditions for max odd/even command
    elif command == 'max':
        max_element = - sys.maxsize
        counter = 0
        for el in range(len(data_to_manipulate)):
            if index == 'odd' and int(data_to_manipulate[el]) % 2 != 0 and int(data_to_manipulate[el]) >= max_element:
                max_element = int(data_to_manipulate[el])
                max_index = el
                counter += 1
            elif index == 'even' and int(data_to_manipulate[el]) % 2 == 0 and int(data_to_manipulate[el]) >= max_element:
                max_element = int(data_to_manipulate[el])
                max_index = el
                counter += 1
        if counter == 0:
            max_index = 'No matches'
        print(max_index)
    # Conditions for min odd/even command
    elif command == 'min':
        min_element = sys.maxsize
        counter = 0
        for el in range(len(data_to_manipulate)):
            if index == 'odd' and int(data_to_manipulate[el]) % 2 != 0 and int(data_to_manipulate[el]) <= min_element:
                min_element = int(data_to_manipulate[el])
                min_index = el
                counter += 1
            elif index == 'even' and int(data_to_manipulate[el]) % 2 == 0 and int(data_to_manipulate[el]) <= min_element:
                min_element = int(data_to_manipulate[el])
                min_index = el
                counter += 1
        if counter == 0:
            min_index = 'No matches'
        print(min_index)
    # Conditions for first {count} odd/even command
    elif command == 'first':
        index = int(index)
        result_first = []

        if index > len(data_to_manipulate) or index < 0:
            print('Invalid count')

        elif type_num == 'odd':
            odd_counter = 0
            for el in range(len(data_to_manipulate)):
                if int(data_to_manipulate[el]) % 2 != 0 and odd_counter < index:
                    result_first.append(data_to_manipulate[el])
                    odd_counter += 1

            result_first = ', '.join(result_first)
            if odd_counter == 0:
                print([])
            else:
                print(f'[{result_first}]', end='')
                print()

        elif type_num == 'even':
            even_counter = 0
            for el in range(len(data_to_manipulate)):
                if int(data_to_manipulate[el]) % 2 == 0 and even_counter < index:
                    result_first.append(data_to_manipulate[el])
                    even_counter += 1

            result_first = ', '.join(result_first)
            if even_counter == 0:
                print([])
            else:
                print(f'[{result_first}]', end='')
                print()


    # Conditions for last {count} odd/even command
    elif command == 'last':
        index = int(index)
        result_last = []
        result_last_final = []

        if index > len(data_to_manipulate) or index < 0:
            print('Invalid count')

        elif type_num == 'odd':
            odd_counter = 0
            for el in range(len(data_to_manipulate) - 1, -1, -1):
                if int(data_to_manipulate[el])% 2 != 0 and odd_counter < index:
                    result_last.append(data_to_manipulate[el])
                    odd_counter += 1
            for i in range(len(result_last) - 1, -1, -1):
                result_last_final.append(result_last[i])

            result_last_final = ', '.join(result_last_final)
            if odd_counter == 0:
                print([])
            else:
                print(f'[{result_last_final}]', end='')
                print()

        elif type_num == 'even':
            even_counter = 0
            for el in range(len(data_to_manipulate) - 1, -1, -1):
                if int(data_to_manipulate[el]) % 2 == 0 and even_counter < index:
                    result_last.append(data_to_manipulate[el])
                    even_counter += 1

            for i in range(len(result_last) - 1, -1, -1):
                result_last_final.append(result_last[i])

            result_last_final = ', '.join(result_last_final)
            if even_counter == 0:
                print([])
            else:
                print(f'[{result_last_final}]', end='')
                print()

    command = input()

data_to_manipulate = ', '.join(data_to_manipulate)
print(f'[{data_to_manipulate}]', end='')