# https://www.hackerrank.com/challenges/alternating-characters/submissions/code/18041687

numstr = int(input().strip())

for i in range(0, numstr):
    str = input().strip()
    if(len(str) < 2):
        print('0')
    deletecount = 0
    for j in range(1, len(str)):
        if(str[j] == str[j - 1]):
            deletecount += 1
    print(deletecount)
