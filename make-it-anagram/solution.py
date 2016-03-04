# https://www.hackerrank.com/challenges/make-it-anagram/submissions/code/18041497

s1 = input().strip()
s2 = input().strip()

def getCharMap(s):
    map = {}
    for c in s:
        if not c in map.keys():
            map[c] = 0
        map[c] += 1
    return map

def getCommonKeys(dict1, dict2):
    return list(set(dict1.keys()).intersection(dict2.keys()))

def findKeysDoNotBelong(keys, belongTo):
    return [k for k in keys if not k in commonKeys]

def getValueSum(keys, dict):
    sum = 0
    for k in keys:
        sum += dict[k]
    return sum

s1map = getCharMap(s1)
s2map = getCharMap(s2)

commonKeys = getCommonKeys(s1map, s2map)

otherKeysInS1 = findKeysDoNotBelong(s1map.keys(), commonKeys)
otherKeysInS2 = findKeysDoNotBelong(s2map.keys(), commonKeys)

removelCount = getValueSum(otherKeysInS1, s1map) + getValueSum(otherKeysInS2, s2map)

for k in commonKeys:
    removelCount += abs(s1map[k] - s2map[k])
    
print(removelCount)
