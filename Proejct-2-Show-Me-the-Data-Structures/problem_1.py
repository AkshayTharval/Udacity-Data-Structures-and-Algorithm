from collections import OrderedDict

class LRU_Cache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        
        # We will be caching the values in OrderedDict from collection
        self.cache = OrderedDict()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key in self.cache:
            output = self.cache.pop(key)
            
            # Re-insert the value so that cache will reflect latest use
            self.cache[key] = output
            return output
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        
        if self.capacity == 0:
            print('Cannot perform set as capacity is set to {}'.format(self.capacity))
            return
        
        if key in self.cache:

            # Pop and Re-insert the value so that cache will reflect latest use
            self.cache.pop(key)
            self.cache[key] = value
        
        else:
            # In case there is space in cache
            if self.capacity > len(self.cache):
                self.cache[key] = value
            
            else:
                # When using popitem function of OrderedDict,
                # Pairs are returned in LIFO order if last is true or FIFO order if false.
                self.cache.popitem(last=False)
                self.cache[key] = value
                
# Test set provided by Udacity
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry


# Self test cases

our_cache = LRU_Cache(0)
our_cache.set(1, 1)            
# Should return statement "Cannot perform set as capacity is set to 0"
# We can also raise error if required