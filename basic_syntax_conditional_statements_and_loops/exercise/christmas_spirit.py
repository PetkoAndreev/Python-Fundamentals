quantity = int(input())
days = int(input())
ornament_set_price = 2
tree_skirt_price = 5
tree_garlands_price = 3
tree_lights_price = 15
budget = 0
spirit = 0
ornament_set = 0
tree_skirt = 0
tree_garlands = 0
tree_lights = 0

for i in range(1, days + 1):

    if i % 11 == 0:
        quantity += 2

    if i % 2 == 0:
        ornament_set = (quantity * ornament_set_price)
        budget += ornament_set
        spirit += 5

    if i % 3 == 0:
        tree_skirt = (quantity * tree_skirt_price)
        tree_garlands = (quantity * tree_garlands_price)
        budget += tree_skirt + tree_garlands
        spirit += 13

    if i % 5 == 0:
        tree_lights = (quantity * tree_lights_price)
        budget += tree_lights
        spirit += 17
        if i % 3 == 0:
            spirit += 30

    if i % 10 == 0:
        spirit -= 20
        tree_skirt = (1 * tree_skirt_price)
        tree_garlands = (1 * tree_garlands_price)
        tree_lights = (1 * tree_lights_price)
        budget += tree_skirt + tree_garlands + tree_lights
        if i == days:
            spirit -= 30

print(f'Total cost: {budget}')
print(f'Total spirit: {spirit}')