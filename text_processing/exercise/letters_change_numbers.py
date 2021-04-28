from sys import maxsize
str_seq = input().split()
total_sum = 0

for el in str_seq:
    num = ''
    min_index = maxsize
    max_index = -maxsize
    for i in range(len(el)):
        if el[i].isdigit():
            num += el[i]
        elif el[i].isalpha():
            if i < min_index:
                min_index = i
            elif i > max_index:
                max_index = i
    num = float(num)
    # Letter before the number
    if el[min_index].isupper():
        total_sum += num / (ord(el[min_index])-64)
    else:
        total_sum += num * (ord(el[min_index])-96)
    # Letter after the number
    if el[max_index].isupper():
        total_sum -= (ord(el[max_index])-64)
    else:
        total_sum += (ord(el[max_index])-96)

print(f'{total_sum:.2f}')