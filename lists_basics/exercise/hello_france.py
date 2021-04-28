price_data = input().split('|')
budget = float(input())
total_items = []

for price in price_data:
    product_type, product_price = price.split('->')
    product_price = float(product_price)

    if product_type == 'Clothes' and product_price > 50:
        continue
    elif product_type == 'Shoes' and product_price > 35:
        continue
    elif product_type == 'Accessories' and product_price > 20.5:
        continue

    if budget >= product_price:
        total_items.append(product_price)
        budget -= product_price

for item in total_items:
    print(f'{item + (0.4 * item):.2f}', end = ' ')
print()
print(f'Profit: {0.4 * sum(total_items):.2f}')
if sum(total_items) + (0.4 * sum(total_items)) + budget >= 150:
    print('Hello, France!')
else:
    print('Time to go.')