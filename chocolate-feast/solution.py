# https://www.hackerrank.com/challenges/chocolate-feast/submissions/code/18269020
#!/bin/python3

import math

def get_bonus_candies(num_bought, m):
    if num_bought < m:
        # no extra wrappers
        return 0
    bonus = math.floor(num_bought / m)
    left_over = num_bought % m
    wrappers = bonus + left_over
    result = bonus + get_bonus_candies(wrappers, m)
    return result

t = int(input().strip())
for a0 in range(t):
    n,c,m = input().strip().split(' ')
    n,c,m = [int(n),int(c),int(m)]
    
    num_bought = math.floor(n / c)
    result = num_bought + get_bonus_candies(num_bought, m)
    print(result)
