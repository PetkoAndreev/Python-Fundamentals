targets = [int(s) for s in input().split()]
command = input()
shot_targets = 0

while command != 'End':
    target = int(command)
    if target in range(len(targets)):
        for i in range(len(targets)):
            if targets[i] != -1 and i != target and targets[i] > targets[target]:
                targets[i] -= targets[target]
            elif targets[i] != -1 and i != target and targets[i] <= targets[target]:
                targets[i] += targets[target]
        targets[target] = -1
        shot_targets += 1
    command = input()

print(f'Shot targets: {shot_targets} -> ', end = '')
print(*targets, sep = ' ')