first_str = input()
second_str = input()

result_string = ""

for iteration in range(len(first_str)):
    for index_str2 in range(0, iteration + 1):
        result_string += second_str[index_str2]
    for index_str1 in range(iteration + 1, len(first_str)):
        result_string += first_str[index_str1]
    if second_str[index_str2] != first_str[iteration]:
        print(result_string)
        result_string = ""
    result_string = ""