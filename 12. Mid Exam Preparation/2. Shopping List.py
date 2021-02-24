shop_list = input().split('!')
command = input()

while command != 'Go Shopping!':
    if 'Correct' in command:
        command, old_item, new_item = command.split()
    else:
        command, item = command.split()

    if command == 'Urgent':
        if item not in shop_list:
            shop_list.insert(0, item)
    elif command == 'Unnecessary':
        if item in shop_list:
            shop_list.remove(item)
    elif command == 'Rearrange':
        if item in shop_list:
            shop_list.remove(item)
            shop_list.append(item)
    elif command == 'Correct':
        if old_item in shop_list:
            for i in range(len(shop_list)):
                if shop_list[i] == old_item:
                    shop_list[i] = new_item

    command = input()

print(', '.join(shop_list))