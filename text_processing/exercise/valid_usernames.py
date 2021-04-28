users = input().split(', ')

for user in users:
    counter = 0
    if len(user) in range(3, 17):
        if user.isalnum():
            print(user)
        else:
            for el in user:
                if el.isdigit():
                    counter += 1
                elif el.isalpha():
                    counter += 1
                elif el == '-' or el == '_':
                    counter += 1
            if counter == len(user):
                print(user)