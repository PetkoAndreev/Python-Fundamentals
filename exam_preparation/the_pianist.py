num_pieces = int(input())
pieces = {}

for i in range(1, num_pieces + 1):
    piece, composer, key = input().split('|')
    pieces[piece] = [composer, key]

data = input()

while data != 'Stop':
    data = data.split('|')
    command = data[0]

    if command == 'Add':
        piece = data[1]
        composer = data[2]
        key = data[3]
        if piece in pieces:
            print(f'{piece} is already in the collection!')
        else:
            pieces[piece] = [composer, key]
            print(f'{piece} by {composer} in {key} added to the collection!')

    elif command == 'Remove':
        piece = data[1]
        if piece in pieces:
            print(f'Successfully removed {piece}!')
            del pieces[piece]
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')

    elif command == 'ChangeKey':
        piece = data[1]
        new_key = data[2]
        if piece in pieces:
            pieces[piece][1] = new_key
            print(f'Changed the key of {piece} to {new_key}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')

    data = input()

pieces = dict(sorted(pieces.items(), key=lambda s: (s[0], s[1][0])))

for piece, value in pieces.items():
    composer = value[0]
    key = value[1]
    print(f'{piece} -> Composer: {composer}, Key: {key}')