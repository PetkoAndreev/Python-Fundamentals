input_data = input().split()
dict_res = {}

for el in input_data:
    value = 1
    for i in range(len(el)):
        key = el[i]
        if key not in dict_res:
            dict_res[key] = value
        else:
            dict_res[key] += 1
for key, value in dict_res.items():
    print(f'{key} -> {value}')