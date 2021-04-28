import re

while True:
    input_data = input().strip()

    if input_data == "":
        break

    pattern = r"\d+"

    result = re.findall(pattern, input_data)
    if result == []:
        continue
