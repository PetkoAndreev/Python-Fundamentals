command = input()
force_users = {}


def command_line(side, user):
    user_found = False
    for sides, users in force_users.items():
        if user in users:
            user_found = True
    if not user_found:
        if side not in force_users:
            force_users[side] = [user]
        else:
            if user not in force_users[side]:
                force_users[side].append(user)
    return force_users


def command_sign(side, user):
    for sides, users in force_users.items():
        if user in users:
            users.remove(user)
    if side not in force_users:
        force_users[side] = [user]
        print(f'{user} joins the {side} side!')
    else:
        if user not in force_users[side]:
            force_users[side].append(user)
            print(f'{user} joins the {side} side!')
    return force_users


while command != 'Lumpawaroo':
    if '|' in command:
        side, user = command.split(' | ')
        command_line(side, user)
    elif '->' in command:
        user, side = command.split(' -> ')
        command_sign(side, user)
    else:
        break
    command = input()

force_users = dict(sorted(force_users.items(), key=lambda s: (-len(s[1]), s[0])))

for side, user in force_users.items():
    if user != []:
        user = user.sort()

for side, user in force_users.items():
    if user != []:
        print(f'Side: {side}, Members: {len(user)}', end='\n! ')
        print('\n! '.join(user))