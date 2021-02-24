import re
input_data = input().lower()
key_word = input().lower()

pattern = rf'\b{key_word}(?=[^a-zA-Z0-9]|$)|(?<=[^a-zA-Z0-9]){key_word}(?=[^a-zA-Z0-9]|$)'
result = re.findall(pattern, input_data)
print(result.count(key_word))