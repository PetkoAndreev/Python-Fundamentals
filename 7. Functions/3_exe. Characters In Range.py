def ascii_characters(start, end):
    symbol_data = []
    for symbol in range(ord(start) + 1, ord(end)):
        symbol = symbol_data.append(chr(symbol))
    return ' '.join(symbol_data)

start_symbol = input()
end_symbol = input()

print(ascii_characters(start_symbol, end_symbol))