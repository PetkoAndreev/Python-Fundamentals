import math
numbers = [int(s) for s in input().split(', ')]

for i in range(1, math.ceil(max(numbers) /10 + 1)):
    result = [numbers[num] for num in range(len(numbers)) if numbers[num] in range(i * 10 - 10 + 1, i * 10 + 1)]
    print(f'Group of {i * 10}\'s: {result}')