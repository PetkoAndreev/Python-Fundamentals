import re

data = input()
pattern = r'(?P<separator>\||#)(?P<item>[a-zA-Z\s]+)(?P=separator)(?P<date>(\d{2}/){2}\d{2})(?P=separator)(?P<calories>(\d{1,4}|10000))(?P=separator)'
food_storage = []
total_calories = 0
result = re.finditer(pattern, data)

for match in result:
    items = match.groupdict()
    total_calories += int(items['calories'])
    food_storage.append(items)


days = total_calories // 2000
print(f'You have food to last you for: {days} days!')


for item in food_storage:
    print(f'Item: {item["item"]}, Best before: {item["date"]}, Nutrition: {item["calories"]}')