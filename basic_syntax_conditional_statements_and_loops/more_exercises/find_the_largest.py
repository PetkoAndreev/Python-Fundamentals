number = input()

number_list = []
max_num = ''

for i in range(len(number)):
    number_list.append(int(number[i]))

while number_list:
    num_index_to_remove = number_list.index(max(number_list))
    max_num += str(number_list.pop(num_index_to_remove))

print(int(max_num))