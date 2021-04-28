data = input()

capital_indexes = []

for i in range(len(data)):
    if data[i].isupper():
        capital_indexes.append(i)

print(capital_indexes)