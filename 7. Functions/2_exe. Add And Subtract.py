def sum_numbers():
    sum_nums = 0
    for i in range(2):
        current_num = int(input())
        sum_nums += current_num
    return sum_nums


def subtract_numbers():
    subtract_num = int(input())
    return subtract_num


def add_subtract_numbers():
    result = sum_numbers() - subtract_numbers()
    return result


print(add_subtract_numbers())
