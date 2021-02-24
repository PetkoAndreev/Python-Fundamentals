substring_data = input().split(', ')
string_data = input()

result = [el for el in substring_data if el in string_data]
print(result)