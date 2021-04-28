num1 = input()
num2 = input()
nums = [num1, num2]

result = ''
result += 'Before:\n'
result += f'a = {nums[0]}\n'
result += f'b = {nums[1]}\n'
result += 'After:\n'
result += f'a = {nums[1]}\n'
result += f'b = {nums[0]}'
print(result)
