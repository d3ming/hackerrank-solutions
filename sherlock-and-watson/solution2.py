"""
# Rotate array with recursion
# will hit stack overflow on large rotate/arrays
def rotate_array(input_array, num_rotates):
    if num_rotates == 0:
        return input_array
    length = len(input_array)
    last = input_array[length-1]
    new_array = [last]
    new_array += input_array[:length-1]
    #print(new_array)
    return rotate_array(new_array, num_rotates - 1)
"""

"""
# Rotate array with for loop
# Will hit timeout issues...
def rotate_array(input_array, num_rotates):
    length = len(input_array)    
    if num_rotates > length:
        num_rotates = num_rotates % length
    for i in range(num_rotates):    
        last = input_array[length-1]
        new_array = [last]
        new_array += input_array[:length-1]
        input_array = new_array
    return new_array
"""


def get_value_after_rotate(input_array, num_rotates, index):    
    '''
    The right solution is one where we don't rotate the array
    and just calculate the new index
    '''
    length = len(input_array)
    if num_rotates > length:
        num_rotates = num_rotates % length
        
    shift = length - num_rotates
    normalized_index = (index + shift) % length
    return input_array[normalized_index]

# MAIN ROUTINE:
line1 = input().strip().split()
num_int = int(line1[0])
num_rotates = int(line1[1])
num_queries = int(line1[2])

line2 = input().strip().split()
input_array = [int(value) for value in line2]

for i in range(num_queries):
    index = int(input().strip())
    print(get_value_after_rotate(input_array, num_rotates, index))
