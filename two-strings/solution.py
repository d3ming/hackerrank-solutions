# https://www.hackerrank.com/challenges/two-strings/copy-from/18008663
num_tests = int(input().strip())

for i in range(0, num_tests):
    s1 = input().strip()
    s2 = input().strip()
    # as long as one char in s2 is contained in s1, answer is YES
    mapfors1 = {}
    for j in range(0, len(s1)):
        if not s1[j] in mapfors1:
            mapfors1[s1[j]] = 1
    exist = False
    for k in range(0, len(s2)):
        if s2[k] in mapfors1:
            print('YES')
            exist = True
            break
    if not exist:
        print('NO')
