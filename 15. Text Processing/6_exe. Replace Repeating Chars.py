input_sequence = input()
result = []
for i in range(len(input_sequence)):
    if i < len(input_sequence) - 1 and input_sequence[i] != input_sequence[i+1]:
        result.append(input_sequence[i])
result.append(input_sequence[-1])

print(''.join(result))