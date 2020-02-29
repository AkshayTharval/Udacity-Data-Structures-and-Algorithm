class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def linkedlist_to_list(linked_list):
    """ Function to convert linkedlist object into list """
    if linked_list.head == None:
        return []
    
    output_list = []
    current_node = linked_list.head
    while current_node:
        output_list.append(current_node.value)
        current_node = current_node.next
    
    return output_list
        
def list_to_linkedlist(input_list):
    """ Function to convert list into linkedlist object """
    if len(input_list) == 0:
        return LinkedList()
    
    output_linked_list = LinkedList()
    for info in input_list:
        output_linked_list.append(info)
    
    return output_linked_list
    
def union(llist_1, llist_2):
    """ Output union between two linkedlists"""
    return list_to_linkedlist(list(set(linkedlist_to_list(llist_1)) | set(linkedlist_to_list(llist_2))))

def intersection(llist_1, llist_2):
    """ Output intersection between two linkedlists"""
    return list_to_linkedlist(list(set(linkedlist_to_list(llist_1)) & set(linkedlist_to_list(llist_2))))


# Test case 1
print("================================== Test Case 1 ==================================")
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print("{} U {}:".format(element_1, element_2))
print (union(linked_list_1,linked_list_2))
# Output:
# 32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 -> 
print()
print("{} ∩ {}:".format(element_1, element_2))
print (intersection(linked_list_1,linked_list_2))
# Output:
# 4 -> 21 -> 6 -> 

# Test case 2
print("================================== Test Case 2 ==================================")
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print("{} U {}:".format(element_1, element_2))
print (union(linked_list_3,linked_list_4))
# Output:
# 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 -> 
print()
print("{} ∩ {}:".format(element_1, element_2))
print (intersection(linked_list_3,linked_list_4))
# Output:
# 

print("================================== Edge Cases ==================================")
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print("{} U {}:".format(element_1, element_2))
print(union(linked_list_5, linked_list_6))
# Output:
#
print()
print("{} ∩ {}:".format(element_1, element_2))
print(intersection(linked_list_5, linked_list_6))
# Output:
#