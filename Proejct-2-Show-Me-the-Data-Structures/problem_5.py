import hashlib
import time

class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_block = None
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = self.data.encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()

    # Function for printing an object in a string when print function is called
    # Reference: https://docs.python.org/3/library/functions.html#repr
    def __repr__(self):
        return 'Block Information: \n Data: {} \n Timestamp: {} \n Hash: {}'.format(self.data, self.timestamp, self.hash)
    

class BlockChain(object):
    def __init__(self):
        self.head = None
        
    def append(self, value):
        """ We are keeping track of the last added block in this class"""
        
        if self.head == None: # If blockchain is empty
            self.head = Block(time.time(), value, None)
        
        else: # Add new block at the end
            new_block = Block(time.time(), value, self.head.hash)
            new_block.previous_block = self.head
            
            self.head = new_block
            
    def size(self):
        """ Return the size or length of the BlockChain. """
        position_head = self.head
        length = 0

        while position_head:
            position_head = position_head.previous_block
            length += 1

        return length
    
    def search(self, value):
        """ Search in blockchain for a particular value"""
        
        # If there are no blocks in blockchain
        if self.head == None:
            print('Please enter value in BlockChain before searching a value')
            return None
        
        node = self.head
        while node:
            if node.data == value:
                return node
            
            node = node.previous_block
        
        return None
    
    def to_list(self):
        """ Print blockchain (linked list) as a list"""
        if self.head == None:
            return []
        
        node = self.head
        output = []
        while node:
            output.append([node.data, node.timestamp, node.hash, node.previous_hash])
            node = node.previous_block
            
        return output
            
# Basic Testing
print("=============================== Basic Testing ===============================")
# Initiating the blockchain
blockchain = BlockChain()

# Printing the initial conditions
print("BlockChain size when initiated: {}".format(blockchain.size()))
# Output: 0
print("BlockChain as a list when initiated: {}".format(blockchain.to_list()))
# Output: []
print("===================================")

# Appedning first information (block)
blockchain.append('my balance: 0 | cash flow: +5 | final balance: 5')
print("BlockChain size after some data is appended: {}".format(blockchain.size()))
# Output: 1
print("BlockChain as a list after some data is appended: \n {}".format(blockchain.to_list()))
# [['my balance: 0 | cash flow: +5 | final balance: 5', 1582154723.86675, '092919bc92d3d730e49e0ed08a4f23d92b525350849a2f98d970431e431f17e1', None]]
print("===================================")

# Appending more information
blockchain.append('Balance: 5 | Debit: +25 | Final: 30')
blockchain.append('Balance: 30 | Debit: -20 | Final: 10')
blockchain.append('Balance: 10 | Debit: +35 | Final: 45')

# Printing information about the blockchain
print("BlockChain size: {}".format(blockchain.size()))
# Output: 4
print("BlockChain in list:")
for info in blockchain.to_list():
    print(info)
# Output:
# BlockChain in list:
# ['Balance: 10 | Debit: +35 | Final: 45', 1582154803.9109848, '8774537e13d6caaac199b30bc4b0cbf8edf3106b2f7c85b4f9c266dc01826296', Block Information: 
#  Data: Balance: 30 | Debit: -20 | Final: 10 
#  Timestamp: 1582154803.9109848 
#  Hash: dd790ac3e5943e904409e8e4d5a5bedc75ac8399c77cdf858a0b21f6bb11f832]
# ['Balance: 30 | Debit: -20 | Final: 10', 1582154803.9109848, 'dd790ac3e5943e904409e8e4d5a5bedc75ac8399c77cdf858a0b21f6bb11f832', Block Information: 
#  Data: Balance: 5 | Debit: +25 | Final: 30 
#  Timestamp: 1582154803.9109848 
#  Hash: 8e781e0b714e74b829b1f279da8f29ddae6984f5d30dedb404fd90d3a3e26acd]
# ['Balance: 5 | Debit: +25 | Final: 30', 1582154803.9109848, '8e781e0b714e74b829b1f279da8f29ddae6984f5d30dedb404fd90d3a3e26acd', Block Information: 
#  Data: my balance: 0 | cash flow: +5 | final balance: 5 
#  Timestamp: 1582154803.9099872 
#  Hash: 092919bc92d3d730e49e0ed08a4f23d92b525350849a2f98d970431e431f17e1]
# ['my balance: 0 | cash flow: +5 | final balance: 5', 1582154803.9099872, '092919bc92d3d730e49e0ed08a4f23d92b525350849a2f98d970431e431f17e1', None]
print("===================================")

# Search for a record
print(blockchain.search('Balance: 30 | Debit: -20 | Final: 10'))
# Output:
# Block Information: 
#  Data: Balance: 30 | Debit: -20 | Final: 10 
#  Timestamp: 1582154911.0442767 
#  Hash: dd790ac3e5943e904409e8e4d5a5bedc75ac8399c77cdf858a0b21f6bb11f832

# Case when a record is not found
print(blockchain.search('Balance: 100 | Debit: -20 | Final: 80'))
# Output: None

# Edge Case:
print("=============================== Edge Case Testing ===============================")
blockchain = BlockChain()
print(blockchain.search('my balance: 20 | cash flow: +125 | final balance: 145'))
# Output:
# Please 'append' data on the BlockChain before searching for it
# None