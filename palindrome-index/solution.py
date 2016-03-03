# https://www.hackerrank.com/challenges/palindrome-index/submissions/code/18007550
## clarifications:
# If the string is already a palindrome, then print −1.
# There will always be a valid solution.
# OPTION: If there are multiple indexes as solutions, return the smallest index (NOT IMPLEMENTED BELOW)

def isPalindrome(target):
    sindex = 0
    eindex = len(target) - 1
    while eindex - sindex > 0:
        if target[sindex] != target[eindex]:
            return False
        eindex -= 1
        sindex += 1
    return True

def getPalindromeIndex(target):
    skipcount = 0
    skipped_sindex = -1
    skipped_eindex = -1
    skipped_index = -1
    sindex = 0
    eindex = len(target) - 1
    while eindex - sindex > 0:
        if target[sindex] != target[eindex]:
            if skipcount == 0:
                # skip sindex by 1
                sindex_at_skipping = sindex
                eindex_at_skipping = eindex
                skipped_index = sindex
                sindex += 1
            elif skipcount == 1:
                # set sindex back to skipindex
                # skip eindex
                sindex = sindex_at_skipping
                eindex = eindex_at_skipping
                skipped_index = eindex
                eindex -= 1
            else:
                print('no result') # should not happen
                return
            skipcount += 1
        else:
            eindex -= 1
            sindex += 1
    print(skipped_index)

num_tests = int(input().strip())
for k in range(0, num_tests):
    getPalindromeIndex(input().strip())

# getPalindromeIndex("aadbbaa")
# test cases: "a","aaba", "acba", "abac", "ab", "abc"
