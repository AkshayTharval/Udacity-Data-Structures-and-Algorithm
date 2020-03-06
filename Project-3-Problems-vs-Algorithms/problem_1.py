import math
def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    
    """
    Solution:
    There are 2 cases to take care of, when a whole number is a perfect square root and when we need to find square
    root between two numbers.
    Eg. case1: sqrt(25) = 5
    case2: sqrt(3) = 1.73205
    
    But since we are providing the floor value of square roots, we will be providing the number befire decimal.
    Hence sqrt(3) will be 1.
    """
    
    # Base cases
    if number == 0:
        return 0
    
    if number == 1:
        return 1
    
    # Edge cases where we can return an error if needed
    if number == None:
        print('Please enter a positive number')
        return None
    
    if number < 0:
        print('Please enter a positive number')
        return None

    output = 0
    start = 0
    end = number
    while True:
        
        # Case 2:
        # If we are within a difference of 1, return the floor number
        if abs(start - end) == 1:
            output = start
            break
        
        mid = (start + end)//2

        square = mid*mid
        
        # Case 1: We find a whole number which is a perfect sqrt of a number
        if (square == number):
            output = mid
            break
            
        elif (square > number):
            end = mid
        
        elif (square < number):
            start = mid
    
    return output
	
# Test Cases provided by Udacity
print("=========================== Normal Cases ===============================")
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

# Edge Cases:
print("=========================== Edge Cases ===============================")
print ("Pass" if  (None == sqrt(None)) else "Fail")
print ("Pass" if  (None == sqrt(-2)) else "Fail")