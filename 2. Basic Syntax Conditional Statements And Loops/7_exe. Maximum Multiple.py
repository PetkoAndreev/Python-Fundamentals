divisor = int(input())
bound = int(input())

for i in range(divisor, bound + 1):
    if i % divisor == 0 and 0 < i <= bound:
        max_multiple = i
print(f'{max_multiple}')