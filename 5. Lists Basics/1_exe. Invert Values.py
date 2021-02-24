input_str = input()
input_list = list(map(int, input_str.split(' ')))
result = []

for el in input_list:
    # convert positive to negative
    if el >= 0:
        result.append(-el)
    # convert negative to positive
    else:
        result.append(-el)

print(result)