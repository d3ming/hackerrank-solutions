# https://www.hackerrank.com/challenges/alternating-characters/copy-from/17940138
t = int(input().strip())

def get_num_repeated(input_string):
    result = 0
    for i in range(1, len(input_string)):
        c = input_string[i]
        if c == input_string[i-1]:
            result += 1
    print(result)
    return result

for i in range(t):
    test_input = str(input().strip())
    result = get_num_repeated(test_input)
