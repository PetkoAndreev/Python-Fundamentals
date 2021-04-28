start_collection = input().split(', ')
command = input()

while command != 'Craft!':
    command, item = command.split(' - ')
    if 'Combine' in command:
        old_item, new_item = item.split(':')
    if command == 'Collect':
        if item not in start_collection:
            start_collection.append(item)
    elif command == 'Drop':
        if item in start_collection:
            start_collection.remove(item)
    elif command == 'Combine Items':
        if old_item in start_collection:
            for i in range(len(start_collection)):
                if start_collection[i] == old_item:
                    start_collection.insert(i + 1, new_item)
                    break
    elif command == 'Renew':
        for i in range(len(start_collection)):
            if start_collection[i] == item and start_collection[len(start_collection) - 1] != item:
                start_collection.append(item)
                start_collection.pop(i)
                break
    command = input()

print(', '.join(start_collection))