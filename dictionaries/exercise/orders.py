product = input()
products = {}

while product != 'buy':
    prd_name, prd_price, prd_quantity = product.split()
    prd_price = float(prd_price)
    prd_quantity = float(prd_quantity)
    if prd_name in products:
        for old_price, old_quantity in products[prd_name].items():
            if old_price != prd_price:
                products[prd_name] = {prd_price: prd_quantity + old_quantity}
            else:
                products[prd_name] = {old_price: prd_quantity + old_quantity}
    else:
        products[prd_name] = {prd_price: prd_quantity}
    product = input()


for product, prd_details in products.items():
    for key, value in prd_details.items():
        print(f'{product} -> {key * value:.2f}')