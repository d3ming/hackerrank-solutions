# https://www.hackerrank.com/challenges/sherlock-and-pairs/submissions/code/17974306
num_tests = int(input().strip())

def countPairs(arr):
    map = {}
    for i in range(0, len(arr)):
        if not arr[i] in map:
            map[arr[i]] = [i]
        else:
            map[arr[i]].append(i)
    count = 0
    for k in map.keys():
        numVals = len(map[k])
        if numVals > 1:
            count += (numVals * (numVals - 1))
    return count
               
for i in range(0, num_tests):
    arr_size = int(input().strip())
    arr = [int(val) for val in input().strip().split(" ")]
    print(countPairs(arr))
