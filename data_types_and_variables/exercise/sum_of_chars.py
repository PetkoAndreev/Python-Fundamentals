num_chars = int(input())
sum_chars = 0

for num in range (1, num_chars + 1):
    char = input()
    sum_chars += ord(char)
print(f'The sum equals: {sum_chars}')