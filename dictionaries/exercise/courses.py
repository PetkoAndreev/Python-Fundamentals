course = input()
courses = {}
courses_count = {}
while course != 'end':
    course, student = course.split(' : ')
    if course in courses:
        courses[course].append(student)
    else:
        courses[course] = [student]
    course = input()
for course, count_students in courses.items():
    courses_count[course] = len(count_students)

courses_count = dict(sorted(courses_count.items(), key=lambda s: s[1], reverse=True))
for key, value in courses.items():
    value.sort()

for key, value in courses.items():
    for i in range(len(value)):
        value[i] = '-- ' + value[i]

for key, value in courses_count.items():
    for course, student_name in courses.items():
        if key == course:
            print(f'{key}: {value}', end='\n')
            print('\n'.join(student_name))
            break