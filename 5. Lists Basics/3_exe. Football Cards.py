cards = input()
counter_a = 0
counter_b = 0
cards_list = list(cards.split())
cards_list_unique = []
for el in cards_list:
    if el not in cards_list_unique:
        cards_list_unique.append(el)

for el in cards_list_unique:
    if 'A' in el:
        if counter_a < 5:
            counter_a += 1
    elif 'B' in el:
        if counter_b < 5:
            counter_b += 1


print(f'Team A - {11 - counter_a}; Team B - {11 - counter_b}')
if 11 - counter_a < 7 or 11 - counter_b < 7:
    print('Game was terminated')