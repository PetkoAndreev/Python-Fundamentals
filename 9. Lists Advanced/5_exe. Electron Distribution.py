input_num = int(input())
result = []
curr_sum = 0
numbers = [2*(s**2) for s in range(1, input_num + 1) if input_num - (2*(s**2)) > 0]

for el in numbers:
    curr_sum += el
    if curr_sum <= input_num:
        if input_num - el >= 0 and curr_sum <= input_num:
            result.append(el)

if input_num - sum(result) > 0:
    result.append(input_num - sum(result))

print(result)