# https://www.hackerrank.com/challenges/pangrams/copy-from/18009370
str = input().strip().lower().replace(" ","")

map = {}
for c in str:
    if not c in map:
        map[c] = 1
if len(map.keys()) == 26:
    print('pangram')
else:
    print('not pangram')
