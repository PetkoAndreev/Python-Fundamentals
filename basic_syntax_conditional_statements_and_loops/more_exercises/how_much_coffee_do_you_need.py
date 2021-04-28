command = input()
coffees = 0
commands_applicable = ['coding', 'dog', 'cat', 'movie']

while command != 'END':
    if command.lower() in commands_applicable:
        if command.isupper():
            coffees += 2
        elif command.islower():
            coffees += 1
    command = input()

if coffees > 5:
    print('You need extra sleep')
else:
    print(coffees)
