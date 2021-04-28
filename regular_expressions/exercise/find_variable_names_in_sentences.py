import re

input_data = input().strip()

pattern = r'(?<=\b_{1})[a-zA-Z0-9]+(?=\s|$)'

result = re.findall(pattern, input_data)

print(','.join(result))