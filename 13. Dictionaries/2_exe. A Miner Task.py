command = input()
prepare_data = []
resources = {}

while command != 'stop':
    prepare_data.append(command)
    command = input()

for i in range(0, len(prepare_data), 2):
    key = prepare_data[i]
    value = int(prepare_data[i + 1])
    if key in resources:
        resources[key] += value
    else:
        resources[key] = value

for key, value in resources.items():
    print(f'{key} -> {value}')