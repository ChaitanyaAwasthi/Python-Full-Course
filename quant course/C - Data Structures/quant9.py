# as we know in a linked list there are no backward references, to solve this problem we have

""" Double Linked list"""

# in this case we have the access to the first node and the last node in O(1)

import collections #collections have the source code of many data structures of python

#double linked list implementation of linked lists
linked_list = collections.deque([])

linked_list.append(10) 
linked_list.append(11) # at the end of the list

linked_list.appendleft(12) # at the beginning of the list 

# pop() returns and removes the right-most item
# popleft() that will remove the left-most item

linked_list.pop() # deque does not take any arguments 
linked_list.popleft()


print(linked_list)




