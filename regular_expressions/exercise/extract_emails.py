import re

input_data = input()

pattern = r'(?<=\s)[a-z0-9]+(\.{1}|-{1}|_{1})?[a-z]+[@]+[a-z]+(-{1}[a-z]+)?[\.][a-z]+([\.][a-z]+-{1}|\.{1}[a-z]+)?'

result = re.finditer(pattern, input_data)
for email in result:
    print(email.group())