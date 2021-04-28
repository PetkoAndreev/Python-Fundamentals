nums = input()
num_elements_to_remove = int(input())
nums_list = list(nums.split())

for index in range(len(nums_list)):
    nums_list[index] = int(nums_list[index])
for iteration in range(1, num_elements_to_remove  + 1):
    nums_list.remove((min(nums_list)))

print(nums_list)