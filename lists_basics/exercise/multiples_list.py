factor = int(input())
count = int(input())
result = []


for iteration in range(1, count + 1):
    result.append(factor * iteration)

print(result)