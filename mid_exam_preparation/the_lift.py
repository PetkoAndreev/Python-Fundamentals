people = int(input())
init_people = people
lift_capacity = input().split()
lift_capacity = [int(s) for s in lift_capacity]

for i in range(len(lift_capacity)):
    if lift_capacity[i] != 0:
        if people >= 4:
            people -= 4 - lift_capacity[i]
            lift_capacity[i] += 4 - lift_capacity[i]
        else:
            if lift_capacity[i] + people <= 4:
                lift_capacity[i] += people
                people -= people
            else:
                lift_capacity[i] = people
                people -= people
    else:
        if people >= 4:
            people -= 4
            lift_capacity[i] = 4
        else:
            lift_capacity[i] = people
            people -= people

lift_capacity = [str(s) for s in lift_capacity]
if people == 0:
    if len(lift_capacity) == lift_capacity.count('4'):
        print(" ".join(lift_capacity))
    else:
        print('The lift has empty spots!')
        print(" ".join(lift_capacity))
else:
    print(f'There isn\'t enough space! {people} people in a queue!')
    print(" ".join(lift_capacity))