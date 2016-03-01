# https://www.hackerrank.com/challenges/game-of-thrones/submissions/code/17940542
test_input = str(input().strip())

def check_charmap(charmap):
    num_odds = 0
    for char in charmap:
        value = charmap[char]
        if value % 2 == 1:
            if num_odds == 1:
                return "NO"
            num_odds += 1
    return "YES"

charmap = {}
for char in test_input:
    if not char in charmap:
        charmap[char] = 0
    charmap[char] += 1
print(check_charmap(charmap))
