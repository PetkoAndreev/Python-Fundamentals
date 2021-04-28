command = input()
languages = {}
users_points = {}

while command != 'exam finished':
    command = command.split('-')
    user = command[0]
    if command[1] != 'banned':
        language = command[1]
        points = int(command[2])
        if language not in languages:
            languages[language] = 1
        else:
            languages[language] += 1
        if user not in users_points:
            users_points[user] = points
        else:
            if points > users_points[user]:
                users_points[user] = points
    else:
        language = command[1]
        users_points.pop(user)

    command = input()

users_points = dict(sorted(users_points.items(), key=lambda s: (-s[1], s[0])))
languages = dict(sorted(languages.items(), key=lambda s: (-s[1], s[0])))

print('Results:')
for user, points in users_points.items():
    print(f'{user} | {points}')

print('Submissions:')
for language, submissions in languages.items():
    print(f'{language} - {submissions}')