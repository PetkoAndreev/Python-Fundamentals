import math

def first_factorial(num):
    return math.factorial(num)

def second_factorial(num):
    return math.factorial(num)

num_1 = int(input())
num_2 = int(input())

print(f'{first_factorial(num_1) / second_factorial(num_2):.2f}')