nums_data = input().split(', ')
beggars = int(input())
beggars_data = []

for beggar in range(beggars):
    beggars_data.append(0)

beggar = 0

while len(nums_data) > 0:
    nums_data[0] = int(nums_data[0])
    if beggar < len(beggars_data):
        beggars_data[beggar] += nums_data[0]
    else:
        beggar = 0
        continue
    nums_data.pop(0)
    beggar += 1

print(beggars_data)