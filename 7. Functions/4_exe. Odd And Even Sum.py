def odd_even_sums(num):
    num = str(num)
    odd_sum = 0
    even_sum = 0
    for i in num:
        i = int(i)
        if i % 2 == 0:
            even_sum += i
        else:
            odd_sum += i

    return f'Odd sum = {odd_sum}, Even sum = {even_sum}'

number = int(input())
print(odd_even_sums(number))