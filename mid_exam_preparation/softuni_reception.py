first_emp = int(input())
second_emp = int(input())
third_emp = int(input())
total_people = int(input())

total_emp = first_emp + second_emp + third_emp
total_hours = 0

while total_people > 0:
    total_hours += 1
    if total_hours % 4 != 0:
        total_people -= total_emp

print(f'Time needed: {total_hours}h.')