import sys

def smallest_number():
    min_num = sys.maxsize
    for i in range(1, 4):
        num = int(input())
        if num < min_num:
            min_num = num
    return min_num

print(smallest_number())