sheeps = input().split(', ')

for i in range(len(sheeps) - 1, -1, -1):
    if sheeps[i] == 'wolf':
        if i == len(sheeps) - 1:
            print('Please go away and stop eating my sheep')
            break
        else:
            sheep_num = len(sheeps[i + 1:])
            print(f'Oi! Sheep number {sheep_num}! You are about to be eaten by a wolf!')
