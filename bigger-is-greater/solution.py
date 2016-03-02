# https://www.hackerrank.com/challenges/bigger-is-greater

## read inputs
num_tests = int(input().strip())
test_cases = []
for i in range(0, num_tests):
    test_cases.append(input().strip())
    
## helpers
# get array of chars from a string
def getCharArr(str):
    ret = []
    for c in str:
        ret.append(c)
    return ret

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def getStr(charArr):
    return ''.join(charArr)

## solve the problem
# reference - https://www.nayuki.io/page/next-lexicographical-permutation-algorithm

def next_permutation(arr):
    # find longest non-increasing suffix
    i = len(arr) - 1;
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1
    # now i is the head index of the suffix

    if i <= 0:
        return False
    
    # array[i - 1] is the pivot
    # find rightmost element that exceeds the pivot
    j = len(arr) - 1;
    while arr[j] <= arr[i - 1]:
        j -= 1
    # now the value array[j] will become the new pivot
    
    # swap the pivot with j
    swap(arr, i - 1, j)
    
    # reverse the suffix
    j = len(arr) - 1
    while i < j:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i += 1
        j -= 1
    
    # successfully computed the next permutation
    return True

for test in test_cases:
    charArr = getCharArr(test)
    if next_permutation(charArr):
        print(getStr(charArr))
    else:
        print('no answer')
