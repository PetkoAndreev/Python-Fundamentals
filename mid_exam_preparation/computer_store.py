input_data = input()
total_price = 0
total_part_price = 0
total_taxes = 0

while input_data not in('special', 'regular'):
    part_price = float(input_data)
    if part_price < 0:
        print('Invalid price!')
    else:
        total_part_price += part_price
        total_taxes += 0.2 * part_price
    input_data = input()
total_price = total_part_price + total_taxes
if input_data == 'special':
    total_price -= 0.1 * total_price
if total_part_price == 0:
    print('Invalid order!')
else:
    print('Congratulations you\'ve just bought a new computer!')
    print(f'Price without taxes: {total_part_price:.2f}$')
    print(f'Taxes: {total_taxes:.2f}$')
    print('-----------')
    print(f'Total price: {total_price:.2f}$')