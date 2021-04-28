input_str = input()
shuffles = int(input())

deck = list(input_str.split())

for i in range (1, shuffles + 1):
    first_half = deck[:len(deck)//2]
    second_half = deck[len(deck)//2:]
    deck = [c for pair in zip(first_half, second_half) for c in pair]
print(deck)