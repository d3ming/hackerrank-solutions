# https://www.hackerrank.com/challenges/almost-sorted
input_size = int(input().strip())
input_raw = input().strip()
input = [int(val) for val in input_raw.split(" ")]

def solve(input):
    sortedInput = sorted(input)
    diffIndexes = []
    for i in range(0, len(input)):
        if sortedInput[i] != input[i]:
            diffIndexes.append(i)
    if len(diffIndexes) < 2:
        print('no')
        return
    if len(diffIndexes) == 2:
        print('yes')
        print('swap {0} {1}'.format(diffIndexes[0] + 1, diffIndexes[1] + 1))
    else:
        temp1 = input[diffIndexes[0]:diffIndexes[len(diffIndexes) - 1] + 1][::-1]
        temp2 = sortedInput[diffIndexes[0]:diffIndexes[len(diffIndexes) - 1] + 1]
        if temp1 == temp2:
            print('yes')
            print('reverse {0} {1}'.format(diffIndexes[0] + 1, diffIndexes[len(diffIndexes) - 1] + 1))
        else:
            print('no')

solve(input)
