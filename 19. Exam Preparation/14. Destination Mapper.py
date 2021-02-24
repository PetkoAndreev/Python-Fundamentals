import re

input_data = input()
pattern = r'(=|/)[A-Z][a-zA-Z]{2,}\1'
destination_list = []
points = 0
if re.finditer(pattern, input_data):
    destinations = re.finditer(pattern, input_data)
    destination_list = [destination.group()[1:-1] for destination in destinations]
    for destination in destination_list:
        points += len(destination)

print(f'Destinations: {", ".join(destination_list)}')
print(f'Travel Points: {points}')