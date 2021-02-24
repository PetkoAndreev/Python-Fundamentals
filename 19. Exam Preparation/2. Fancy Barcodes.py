import re
num_barcodes = int(input())

pattern = r'(@#)(#+)?([A-Z])([a-zA-Z0-9]{5,})(?<=[A-Z])\1\2?'
digit_pattern = r'[0-9]'

for i in range(1, num_barcodes + 1):
    barcode = input()
    if re.match(pattern, barcode):
        result = re.match(pattern, barcode)
        digits = re.findall(digit_pattern, result.group())
        if digits != []:
            print(f'Product group: {"".join(digits)}')
        else:
            print(f'Product group: 00')
    else:
        print('Invalid barcode')