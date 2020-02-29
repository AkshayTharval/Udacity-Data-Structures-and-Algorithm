import sys
import heapq
import collections

# Task 1: Take a string and determine the relevant frequencies of the characters.
def getFrequencyCounter(a):
    return dict(collections.Counter(a))

# Task 2: Build and sort a list of tuples from lowest to highest frequencies.
def sortFrequenciesInSet(a):
    return [(v, k) for k, v in sorted(a.items(), key=lambda item: item[1], reverse=False)]

# Task 3: Build the Huffman Tree by assigning a binary code to each letter, using shorter codes for the more frequent letters. (This is the heart of the Huffman algorithm.)

# Deifning nodes of Huffman tree
class Node:
    def __init__(self,value, weight):
        """Create node for given symbol and weight."""
        self.left = None
        self.right = None
        self.value = value
        self.weight = weight        
        
    # Changing the default python function
    # Reference: https://docs.python.org/2/library/operator.html#operator.__lt__
    def __lt__(self, other):
        return self.weight < other.weight


# Using the following algorithm
# Referenced: Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein,
# Introduction to Algorithms, Third Edition, MIT Press, 2009
# for i := 1 to n − 1 do
# allocate a new node z
# z.left := x := Extract-Min(Q);
# z.right := y := Extract-Min(Q);
# z.freq := x.freq + y.freq;
# Insert(Q, z);
# end for
# return Extract-Min(Q); {return the root of the tree}

def huffmanTree(data):
    """ Make Huffman tree and return root node """
    # Get sorted list of tuples (frequency, key)
    sorted_list_freq = sortFrequenciesInSet(getFrequencyCounter(data))
    heap = []
    
    # Make a list of Nodes
    for info in sorted_list_freq:
        heap.append(Node(info[1], info[0]))
    
    # Convert the list into a heap (thank you heapq)
    heapq.heapify(heap)
    
    # Using the steps mentioned before the function definition
    while len(heap) != 1:
        Z = Node(None,None)
        Z.left = heapq.heappop(heap)
        Z.right = heapq.heappop(heap)
        Z.weight = Z.left.weight + Z.right.weight
        heapq.heappush(heap, Z)
    return heap

# Task 4: Trim the Huffman Tree (remove the frequencies from the previously built tree)
# Using the explaination provided in below video:
# https://www.youtube.com/watch?v=umTbivyJoiI&t=403s
def huffmanCodes(root):
    """ Get a dictionary of every key and equivalent huffman representation"""

    code = {}
    def getCode(Node, currentCode=""):
        if (Node == None): 
            return
        if (Node.left == None and Node.right == None):
            code[Node.value] = currentCode
        
        # Left is 0
        getCode(Node.left, currentCode + "0")
        # Right is 1
        getCode(Node.right, currentCode + "1")

    getCode(root[0])
    return code

# Task 5: Encode the text into its compressed form.

def huff_encode(data):
    """ Concat all the codes together """
    # Case when there is only one element
    if(len(getFrequencyCounter(data))) == 1:
        return "0"*len(data)

    huff_code = "" 
    root = huffmanTree(data)
    table = huffmanCodes(root)
    for item in data:
        huff_code += table[item]
    return huff_code

def huffman_encoding(data):
    return huffmanTree(data), huff_encode(data)

# Task 6: Decode the text from its compressed form.
# Given the tree and bit string, it will be just going down the tree
# As mentioned before, '0' in Huffman code represents left and 1 represents right
def huffman_decoding(bit_string,root):
    """ Convert Huffman compressed representation back to string """

    # Case when there is only one element
    if(len(getFrequencyCounter(bit_string))) == 1:
        return len(bit_string)*str(root[0].value)

    decode = ""
    n = len(bit_string)
    count = 0
    while count < n:
        current = root[0]
        while current.left != None and current.right != None:
            # As before, 0 is left and 1 is right
            if bit_string[count] == "0":
                current = current.left
            else:
                current = current.right
            count+=1
        decode+=current.value
    return decode


def test(data):
    
    if data in [None, '']:
        print('Cannot perform Huffman coding on None or empty string')
        return None
    
    print ("The size of the data is: {}\n".format(sys.getsizeof(data)))
    print ("The content of the data is: {}\n".format(data))

    tree, encoded_data = huffman_encoding(data)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    
    
if __name__ == "__main__":
    
    print("=================================== Case 1 ===================================")

    data = "The bird is the word"

    test(data)
    
    print("=================================== Case 2 ===================================")

    data = "E"

    test(data)
    
    print("=================================== Case 3 ===================================")

    data = 'EE'

    test(data)
    
    print("=================================== Case 4 ===================================")

    data = 'EEE'

    test(data)
    
    print("=================================== Case 5 ===================================")

    data = None

    test(data)
    
    print("=================================== Case 6 ===================================")

    data = ''

    test(data)
    
    print("=================================== Case 7 (Random Text from Harry Potter) ===================================")

    data = 'October arrived, spreading a damp chill over the grounds and into the castle. Madam Pomfrey, the nurse, was kept busy by a sudden spate of colds among the staff and students. Her Pepperup potion worked instantly, though it left the drinker smoking at the ears for several hours afterward. Ginny Weasley, who had been looking pale, was bullied into taking some by Percy. The steam pouring from under her vivid hair gave the impression that her whole head was on fire.'

    test(data)