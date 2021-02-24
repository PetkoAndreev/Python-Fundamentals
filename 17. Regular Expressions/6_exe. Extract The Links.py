import re

while True:

    input_data = input()
    if input_data == '':
        break
    pattern = r'w{3}\.[a-zA-Z0-9-]+\.[a-z]+(\.[a-z]+)?(\.[a-z]+)?(\.[a-z]+)?'

    result = re.finditer(pattern, input_data)

    for link in result:
        print(link.group())