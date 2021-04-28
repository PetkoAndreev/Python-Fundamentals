nums = []

while True:
    data = input()
    if not data:
        break
    nums.append(int(data))

print(max(nums))