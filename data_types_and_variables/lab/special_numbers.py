numbers = int(input())
res_num = 0
for i in range (1, numbers + 1):
    i = str(i)
    res_num = 0
    for num in range (len(i)):
        res_num += int(i[num])
    if res_num in(5, 7, 11):
        print(f'{i} -> True')
    else:
        print(f'{i} -> False')