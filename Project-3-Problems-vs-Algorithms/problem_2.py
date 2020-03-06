def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    
    # Edge cases:
    if input_list == []:
        print("You entered empty list, please enter a valid list")
        return None
    
    if number == None:
        print("You entered no number to find, please enter a valid number")
        return None
    
    # Method 1: Sort the list and then use binary search
    # Complexity: O(n * log n) + O(log n) which will be O(n * log n)
    # Its specifically mentioned that this should take O(log n)
    
    # Method 2: Finding the index where the rotation begins
    # And then dividing the list into two parts and performing binary search on one of them
    
    pivotpoint = findPivotPoint(input_list, 0, len(input_list))
    
    # This means there is no rotation, hence a simple binary search will be sufficient
    if pivotpoint == -1:
        return binarySearch(input_list, 0, len(input_list), number)
    
    # If we find the number at pivot point
    if input_list[pivotpoint] == number: 
        return pivotpoint 
    
    # If first index is less than number, then it should be between index 0 and pivot point
    if input_list[0] <= number: 
        return binarySearch(input_list, 0, pivotpoint-1, number)
    
    # If first index is greater than number, then it should be between pivot point and last index
    return binarySearch(input_list, pivotpoint+1, len(input_list)-1, number)

def findPivotPoint(arr, start, end): 
      
    # base cases 
    if end < start: 
        return -1
    if end == start: 
        return start 
    
    # Find the mid point
    mid = int((start + end)/2) 
    
    # If mid is less than end index and number at mid index > number at mid index + 1, return mid
    if mid < end and arr[mid] > arr[mid + 1]: 
        return mid 
    # If mid is greater than end index and number at mid index > number at mid index + 1, return mid
    if mid > start and arr[mid] < arr[mid - 1]: 
        return (mid-1) 
    
    # If number at start index is greater than or equal to number at index mid, slice the list
    # From start to mid-1
    if arr[start] >= arr[mid]: 
        return findPivot(arr, start, mid-1)

    # If number at end index is greater than or equal to number at index mid, slice the list
    # From mid + 1 to end
    return findPivot(arr, mid + 1, end) 

# Binary search using recursion
def binarySearch(arr, start, end, key): 
  
    if end < start: 
        return -1
    
    mid = int((start + end)/2) 

    if key == arr[mid]: 
        return mid

    if key > arr[mid]:
        return binarySearch(arr, (mid + 1), end, key)

    return binarySearch(arr, start, (mid -1), key)

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")
		
		
# Test Cases provided by Udacity
print("================================= Normal Cases =================================")
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

print("================================= Edge Cases =================================")
test_function([[6, 7, 8, 1, 2, 3, 4], None])
test_function([[], 10])