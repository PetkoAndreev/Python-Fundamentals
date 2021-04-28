import re

furnitures = []
total_amount = 0
pattern = r'>>(?P<product>[A-Za-z]+)<<(?P<price>\d+(\.\d+)?)!(?P<quantity>\d+)(?!.)'
furniture = input()

while furniture != 'Purchase':
    if re.match(pattern, furniture):
        data = re.match(pattern, furniture)
        product, price, quantity = data.group('product', 'price', 'quantity')
        furnitures.append(product)
        total_amount += float(price) * int(quantity)
    furniture = input()

print('Bought furniture:')
[print(item) for item in furnitures]
print(f'Total money spend: {total_amount:.2f}')