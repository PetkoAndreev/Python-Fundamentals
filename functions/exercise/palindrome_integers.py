def palindrome_integers(num):
    for i in range(len(num)):
        number = num[i]
        number_back = ''
        for el_backward in range(len(num[i]) - 1, -1, -1):
            number_back += num[i][el_backward]
        if number == number_back:
            res = True
        else:
            res = False
        print(res)

number = input().split(', ')
palindrome_integers(number)