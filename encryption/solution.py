#!/bin/python3
# https://www.hackerrank.com/challenges/encryption

import sys
import math

s = input().strip()
l = len(s)

sqrt_l = math.sqrt(l)
rows = math.floor(sqrt_l)
cols = math.ceil(sqrt_l)
# it's OK for rows to == cols, for when we need to make it fit the string
if (rows * cols) < l:
    rows += 1

# Split string into substrings per column width
s_list = []
for i in range(rows):
    line = s[:cols]
    s_list.append(line)
    s = s[cols:]

# Assemble result strings based on r index
output = ''
for c in range(cols):
    result = ''
    for s1 in s_list:
        if c < len(s1):
            result += s1[c]
        else:
            continue
    output += result + ' '

output = output.strip()
print(output)
