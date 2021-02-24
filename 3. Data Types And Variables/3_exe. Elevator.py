num_people = int(input())
capacity_elevator = int(input())
total_courses = 0

if num_people / capacity_elevator <= 1:
    total_courses += int(num_people / capacity_elevator)
elif num_people % capacity_elevator == 0:
    total_courses += num_people // capacity_elevator
else:
    total_courses += num_people // capacity_elevator + 1

print(total_courses)