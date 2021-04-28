chairs = int(input())
free_chairs = 0
count_x = 0
sum_chairs = 0
current_room = 0

chairs_data = [input().split() for s in range(1, chairs + 1)]

for el in chairs_data:
    num_x, chairs = el[0], el[1]
    chairs = int(chairs)
    count_x += len(num_x)
    sum_chairs += chairs
    current_room += 1
    if len(num_x) > chairs:
        free_chairs += len(num_x) - chairs
    elif len(num_x) < chairs:
        print(f'{chairs - len(num_x)} more chairs needed in room {current_room}')
if count_x >= sum_chairs:
    print(f'Game On, {free_chairs} free chairs left')