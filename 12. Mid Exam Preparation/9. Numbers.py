numbers = [int(s) for s in input().split()]

avg_num = sum(numbers) / len(numbers)
numbers = sorted(numbers, reverse=True)
numbers = [int(s) for s in numbers if s > avg_num][:5]

if numbers == []:
    print('No')
else:
    print(*numbers, sep=' ')