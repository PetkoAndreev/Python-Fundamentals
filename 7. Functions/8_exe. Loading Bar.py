def loading_bar(num):
    result = []
    for i in range(1, 11):
        result.append('.')

    for perc in range(len(result)):
        if perc < num // 10:
            result[perc] = '%'
    res_data = ''.join(result)
    if num // 10 == 10:
        return f'100% Complete!\n[{res_data}]'
    else:
        return f'{num}% [{res_data}]\nStill loading...'

number = int(input())
print(loading_bar(number))