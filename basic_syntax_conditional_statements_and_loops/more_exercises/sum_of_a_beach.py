data = input()

words_to_search = ["Sand", "Water", "Fish", "Sun"]
count = 0

for word in words_to_search:
    count += data.lower().count(word.lower())

print(count)
