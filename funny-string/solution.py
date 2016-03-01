#https://www.hackerrank.com/challenges/funny-string

num_input = int(input().strip())

def getAlphaMap():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alpha_map = {}
    for i in range(0, len(alphabet)):
        alpha_map[alphabet[i]] = i
    return alpha_map

def getSolution():
    alpha_map = getAlphaMap()
    for i in range(0, num_input):
        s = input().strip()
        r = s[::-1]
        result = 'Funny'
        for j in range (1, len(s)):
            if abs(alpha_map[s[j]] - alpha_map[s[j-1]]) != abs(alpha_map[r[j]] - alpha_map[r[j-1]]):
                result = 'Not Funny'
                break;
        print(result)
        
getSolution()