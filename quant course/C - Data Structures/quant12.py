"""Sets"""

# implemented with the help of a dictionary - it uses arrays under the hood 
# sets are unordered and un-indexed : we do not know the position of the items 
# we can't store duplicates 

set1 = {"hell", "heaven", 213.45, 45, False} 
print(set1) 

# we can also use the set function
set2 = set(("hello", 34))

# if we re-run the code, the order of the set would change as it's unordered 
# we can't use random indexing 

"""checking whether a given item is in a set or not
O(1) costant running time complexity"""

if 334 in set2: 
    print("included")
else:
    print(False)


# question - How is it O(1) running time complexity 
"""Hashing: When an item is added to the set, its hash value is computed using a hash function. 
The hash function takes the item as input and produces a unique numeric value. 
This hash value is used as the index to store the item in the hash table.

Storing: The item is then stored in the hash table at the index corresponding to its hash value. 
If there is already an item stored at that index (collision), 
various collision resolution techniques are employed, such as chaining or open addressing.

Retrieving: When you want to check whether a given item is in the set or not,
 the same hash function is applied to the item to obtain its hash value. 
 The hash value is used to look up the index in the hash table. If an item is found at that index, 
    it means the item exists in the set. If the index is empty or contains a different item, then the given item is not in the set."""


# we can also add items to the set 

set1.add(" new item ")

# we can append multiple items with the help of  update() function
set1.update(["new item", 55]) # the order does not matter and will be appended on a random order


# remove() and discard() 
# both are used to remove items but, if you use remove() and the item is not there in the list there will be an error shown which is not the case for discard()


# pop () function - will return the last item - basically a random item from the set and sets are unordered 
print(set2.pop())

# Union Function - will join two sets 

set3 = {12, 3, 5, 6, 2}
set4 = {3455, 656, 5, 56, 3}
result = set3.union(set4)
print(result)
set5 = {3, 3, 3} # in this python would only store (1) 3 as sets don't store duplicated 


# when you wanna find the union of set4 U set3 

result1 = set4.union(set3)


