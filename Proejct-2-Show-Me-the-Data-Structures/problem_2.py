import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    # In case suffix entered is empty string
    # We can raise an error as well if needed
    if suffix == '':
        print('Please enter a valid suffix')
        return []
    
    if len(os.listdir(path)) == 0: # Base condition during recursion
        return []
    
    files = [_ for _ in os.listdir(path) if '.' + suffix in _]
    folders = [_ for _ in os.listdir(path) if '.' not in _]

    # Recursively calling to check folders
    for folder in folders:
        files.extend(find_files(suffix, path + '\\' + folder))
    
    return files

parent_path = os.getcwd() + '\\testdir'

# Test as mentioned in the problem statement
print(find_files(suffix='c', path=parent_path))
# Output: ['t1.c', 'a.c', 'a.c', 'b.c']

# Self test #1
print(find_files(suffix='h', path=parent_path))
# Output: ['t1.h', 'a.h', 'a.h', 'b.h']

# Self test #2
print(find_files(suffix='a', path=parent_path))
# Output: []

# Self test #3 (Edge case)
print(find_files(suffix='', path=parent_path))
# Output: Please enter a valid suffix
# Output: []