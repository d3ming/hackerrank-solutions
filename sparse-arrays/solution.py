# https://www.hackerrank.com/challenges/sparse-arrays/submissions/code/17940978
def count_query_in_inputs(query_string, inputs):
    result = 0
    for input_str in inputs:
        if query_string == input_str:
            result += 1
    return result

# MAIN ROUTINE
t = int(input().strip())
inputs = []
for i in range(t):
    input_string = str(input().strip())
    inputs.append(input_string)
    
qt = int(input().strip())
for qi in range(qt):
    query_string = str(input().strip())
    result = count_query_in_inputs(query_string, inputs)
    print(result)
