import sys
num_snowballs = int(input())
snowball_value = 0
total_snow = 0
total_time = 0
total_quality = 0
res_value = -sys.maxsize

for ball in range (1, num_snowballs + 1):
    prev_snowball = snowball_value
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = (int(snowball_snow / snowball_time)) ** snowball_quality
    if snowball_value > res_value:
        res_value  = snowball_value
        res_snow = snowball_snow
        res_time = snowball_time
        res_quality = snowball_quality

print(f'{res_snow} : {res_time} = {res_value} ({res_quality})')