budget = float(input())
flavour_price = float(input())
eggs_price = 0.75 * flavour_price
milk_price = flavour_price + (0.25 * flavour_price)
milk_cozonac_price = milk_price / 4
cozonac_price = flavour_price + eggs_price + milk_cozonac_price
cozonacs = 0
color_eggs = 0

while budget > cozonac_price:
    budget -= cozonac_price
    cozonacs += 1
    color_eggs += 3
    if cozonacs % 3 == 0:
        color_eggs -= (cozonacs - 2)

print(f'You made {cozonacs} cozonacs! Now you have {color_eggs} eggs and {budget:.2f}BGN left.')