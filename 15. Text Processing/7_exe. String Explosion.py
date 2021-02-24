explosion = input().split('>')
strength = 0
result = []
for el in explosion:
    for i in range(len(el)):
        if strength > 0 and not el[i].isdigit():
            el[i].replace(el[i], '')
            strength -= 1
        elif el[i].isdigit():
            strength += int(el[i]) - 1
            result.append('>')
        else:
            result.append(el[i])
print(''.join(result))