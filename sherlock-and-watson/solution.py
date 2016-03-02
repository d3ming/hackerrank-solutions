# https://www.hackerrank.com/challenges/sherlock-and-watson/submissions/code/17974688

nkq = input().strip().split(" ")
n = int(nkq[0]) # size of arr
k = int(nkq[1]) # num of ops
q = int(nkq[2]) # num of queries
arr = [int(i) for i in input().strip().split(" ")]
queries = []
for i in range(0, q):
    queries.append(int(input().strip()))
    
def rotate(arr, n, k):
    rotatedArr = [-1] * n
    for oldIndex in range(0, n):
        newIndex = (oldIndex + k % n) % n
        rotatedArr[newIndex] = arr[oldIndex]
    return rotatedArr

arr_rotated = rotate(arr, n, k)
for q in queries:
    print(arr_rotated[q])
