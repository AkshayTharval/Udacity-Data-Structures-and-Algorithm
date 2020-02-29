# Project 2 exaplanations

## Problem 1: LRU Cache implementation

Here, the main data structure used is a Dictionary, more specifically OrderedDict available through 'collections' package in Python. According to the class explanation:
* 'Dictionary that remembers insertion order'
* An inherited dict maps keys to values.
* The inherited dict provides __getitem__, __len__, __contains__, and get.
* The remaining methods are order-aware.
* Big-O running times for all methods are the same as regular dictionaries.
* The internal self.__map dict maps keys to links in a doubly linked list.
* The circular doubly linked list starts and ends with a sentinel element.
* The sentinel element never gets deleted (this simplifies the algorithm).
* The sentinel is in self.__hardroot with a weakref proxy in self.__root.
* The prev links are weakref proxies (to prevent circular references).
* Individual links are kept alive by the hard reference in self.__map.
* Those hard references disappear when a key is deleted from an OrderedDict.

Due to these features, it was the perfect data structure for LRU implementation.
OrderedDict also has a function 'popitem()', which has an argument, 'last' which can either make it LIFO (Last In First Out) or FIFO (First In First Out).
From function explanation:
* Pairs are returned in LIFO order if last is true or FIFO order if false.

### Time and Space Complexities:
get() and set() are performed in O(1) because OrderedDict similar to normal dictionaries in python
We are also limiting the size of cache, hence O(n) as mentioned in the problem

## Problem 2: File Recursion

As mentioned in the problem statement, we use the python's 'os' library and leverage its following functions:
* os.listdir(directory): To list all the files and folders
* os.path.join(...): To join two strings to make a path, but works without os.path.join as well. See code.

Once we get the files and folders separate, we can recursively call the same function with each folder.
Extend (by using .extend or '+' operator) to add paths after recursion.

### Time and Space Complexities:
Time complexity here depends on the number of folders and number of files in each folder.  
Hence complexity will be O(w*d) where 'w' is the width (number of folders at each level) and 'd' is the depth (how deep do folders go)
Space complexity is O(n) where n is the number of files with required extension. Also with respect to recursive calls, each call makes its own stack frame and that takes space on call stack.  
That will be another O(n) in worst case. But it keeps the space complexity still at O(n)

## Problem 3: Huffman Coding

Apart from the steps mentioned in the problem statement, I have referenced a few more places to solve this.  
As mentioned in the problem statement,  
* Take a string and determine the relevant frequencies of the characters.  
&nbsp;&nbsp;&nbsp;&nbsp; This is done using Counter function in python's collections library  
* Build and sort a list of tuples from lowest to highest frequencies.  
&nbsp;&nbsp;&nbsp;&nbsp; This is done using sorted function in python  
* Build the Huffman Tree by assigning a binary code to each letter, using shorter codes for the more frequent letters. (This is the heart of the Huffman algorithm.)  
&nbsp;&nbsp;&nbsp;&nbsp; This is done using the following reference: Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein, Introduction to Algorithms, Third Edition, MIT Press, 2009.  
* Trim the Huffman Tree (remove the frequencies from the previously built tree).  
&nbsp;&nbsp;&nbsp;&nbsp; This was done after watching the following video from computerphile on youtube: https://www.youtube.com/watch?v=umTbivyJoiI&t=403s  
* Encode the text into its compressed form.
* Decode the text from its compressed form.

### Time and Space Complexities:
Task 1: Time complexity is O(n) as we go through every character in string. Space complexity is also O(n) as we make a new dict, worst case can be of length 'n' (number of characters)  
Task 2: Sorting in Python is done using Tim sort (last time I checked), this requires O(nlogn) time complexity. Space complexity is O(n) as we need list of same length.  
Task 3: Using the algorithm mentioned in "Introduction to Algorithms" by Cormen and Leiserson, time complexity is O(nlogn). Space complexity as O(n) as well, since we are storing the same number of nodes
Task 4: Trimming the tree will require O(n) time complexity and O(n) space complexity as we are converting tree with nodes into dictionary with same number of keys.
Task 5: Time complexity is O(n) as we go through every key in trimming step and concat all the string together. Space complexity is the order of output from Huffman compressed string (Trimming) (still represented as O(n))
Task 6: Similar to trimming, time complexity is of order of Huffman compressed string (still represented as O(n)) and space complexity is order of original string (still represented as O(n))



## Problem 4: Active Directory

The following imagination helped me solve the problem:

-- **Parent Group**  
---- *Individual 1*  
---- *Individual 2*  
---- **Child Group 1**  
&nbsp;&nbsp;&nbsp;&nbsp;---- *Individual 3*  
&nbsp;&nbsp;&nbsp;&nbsp;---- *Individual 4*  
&nbsp;&nbsp;&nbsp;&nbsp;---- **Child Group 2**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;---- *Individual 5*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;---- *Individual 6*  
---- *Individual 5*  
---- **Child Group 3**  
&nbsp;&nbsp;&nbsp;&nbsp;---- *Individual 7*  
&nbsp;&nbsp;&nbsp;&nbsp;---- *Individual 8*  

Hence within a group there can be multiple groups till we reach some individuals or None. Hence the same function can be called recursively to get the individual we are trying to find.

### Time and Space Complexities:
Time complexity depends on the number of groups (g) and individuals (i), hence it will be denoted as O(g*i)
Since we are using recursion, the space complexity will end up being similar to time complexity, O(g*i) because every recursive call will make its on stack frame and that takes space on call stack  

## Problem 5: BlockChain

According to me and the research I have done regarding blockchains, following functions would be useful for this exercise when we are implementing it with LinkedList:
* Append
* Search
* Size
* to_list

Definition of a block and hashing function was already provided in the problem statement. This implementation of linkedlist was reverse of usual linkedlists. Hence instead of the usual head.next, we were looking at head.previous.
In order to print the object, I have used repr() function and reference is https://docs.python.org/3/library/functions.html#repr

### Time and Space Complexities:
Append is performed in O(1) with respect to Time since we are adding new object to the end
Append is performed in O(1) with respect to Space as we are not storing anything nor are we returning anything

Search is performed in O(n) with respect to Time as we need to loop through all the objects
Search is performed in O(1) with respect to Space as we dont store anything and returning only one object

Size is performed in O(n), with respect to time as we need to loop through all the object to get a count, this can be reduced to O(1) by keeping a count in the blockchain object.
Size is performed in O(1) with respect to space complexity, as we are not storing anything and returning only the size.

to_list is performed in O(n), with respect to time as we need to loop through all the objects and append it to the list
to_list is performed in O(n), with respect to space as we make a new list with size that of linkedlist.



## Problem 6: Union and Intersection

I believe the best part of python is that there are many data types predefined in it which are optimized and ready to use. Hence in this problem, I have decided to convert linkedlists into temporary lists and perform union and intersection and then change the lists back into linkedlists.

### Time and Space Complexities:

Converting linkedlists into list is O(n) with respect to space and time, as we loop through the linkedlist once and make a new list of the same length

Converting lists into linkedlist is O(n) with respect to space and time, as we loop through the linkedlist once and make a new list of the same length

* Union: Time complexity is O(n) where 'n' is the combined number of elements in list1 and list2. Space complexity is O(n) as we make a new list which is combination of list1 and list2 (worst case, its sum of len1 and len2)

* Intersection: Time complexity is O(n) where 'n' is the combined number of elements in list1 and list2. Space complexity is O(n) as we make a new list which is combination of list1 and list2 (worst case, its sum of len1 and len2)