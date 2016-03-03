str = input().strip()

map = {}
for c in str:
    if not c in map:
        map[c] = 1
    else:
        map[c] += 1

num_odd = 0
for k in map.keys():
    if map[k] % 2 == 1:
        num_odd += 1
if num_odd > 1:
    print('NO')
else:
    print('YES')
