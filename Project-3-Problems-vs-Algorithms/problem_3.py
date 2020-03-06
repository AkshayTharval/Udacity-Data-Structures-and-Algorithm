"""
After thinking and trying a few methods, following is the algorithm:
1. Get frequency of every digit from 0 to 9
2. Make two lists which will store the individual numbers 2 output numbers
3. Go from 9 to 0, check if currently the numbers remaining to check in list are even or odd
4. Alternate between number_1 and number_2 depending on even or odd remaining numbers in the list
"""


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    
    len_input = len(input_list)
    
    # Edge case:
    if len_input <= 1:
        return [-1, -1]
    
    # Make a frequency list for numbers from 0 to 9
    frequency_counter = [0] * 10
    
    # Depending on the numbers in input list, enter increase frequency of the respective indices
    for num in input_list:
        frequency_counter[num] += 1
    
    # Check if len of input list is even or odd
    if len_input % 2 == 0:
        even = 1
    else:
        even = 0
    
    # Output numbers
    number_one = []
    number_two = []
    
    for i in range(9,-1,-1):
        # Loop till frequency is 0
        while frequency_counter[i]:
            # Alternate between even and odd
            if even:
                number_one.append(str(i))
                even = 0
            else:
                number_two.append(str(i))
                even = 1
            # Reduce the frequency counter by 1
            frequency_counter[i] -= 1
    
    # Join the numbers in the list to make a number
    return [int(''.join(number_one)), int(''.join(number_two))]
	
def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

# Test Cases provided by Udacity
print("================================= Normal Cases =================================")
test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)

print("================================= Edge Cases =================================")
test_function([[], [-1, -1]])
test_function([[0], [-1, -1]])