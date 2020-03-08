# Here we simply keep a counter of number of 0s, 1s and 2s
# Output list will contain the appropriate number of 0s, 1s and 2s
# Since we are going throug the list only once, the complexity is O(n)
def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    
    if len(input_list) == 0:
        return None
    
    _zero = 0
    _one = 0
    _two = 0
    
    for num in input_list:
        if num == 0:
            _zero += 1
        elif num == 1:
            _one += 1
        else:
            _two += 1
    
    output = []
    for i in range(0,_zero):
        output.append(0)
    
    for j in range(0,_one):
        output.append(1)
    
    for k in range(0,_two):
        output.append(2)
        
    return output
	
def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

# Test Cases provided by Udacity
print("================================= Normal Cases =================================")
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

print("================================= Self Cases =================================")
test_function([0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2])
test_function([0,0,0,1,1,1,2,2,2,0,0,0,1,1,1,2,2,2,0,0,0,1,1,1,2,2,2])
test_function([0,2,1,1,2,0,0,2,1,1,2,0,0,2,1,1,2,0,0,2,1,1,2,0])

print("================================= Edge Cases =================================")
test_function([])