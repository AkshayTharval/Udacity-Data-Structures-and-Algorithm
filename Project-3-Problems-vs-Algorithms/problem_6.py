# We keep a track of min and max while looping through all the numbers in the list

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        return None
    _max = 0
    _min = 999999
    
    for num in ints:
        if num > _max:
            _max = num
        
        if num < _min:
            _min = num
    
    return (_min, _max)
	
## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")