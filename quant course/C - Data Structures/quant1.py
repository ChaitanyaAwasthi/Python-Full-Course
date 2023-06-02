"""Arrays and Lists"""

#it aims to make operations as fast as possible: inserting new items or removing given items from the data structure. 

#all items inside an array are identified with an index 
#the items of an array are located right next to each other in the main memory
# (ram), - they can be accessed by the index 


# we can also store different types of data types in the same array (in the case of py)


#items are located next to each other  so it can be accessed easily- O(1) time complex..


"""this means that 

if you wanna store 4 items in a ram(random access memory) the items will be right
next to each other in the RAM"""

#as it's right next to each other we can calculate the index of items quite easily.
"""memory address = array's address + index * data size (16 byte)"""

#array's address f.e in this case is 0*100

"""two-dimensional array"""

# every single item can be identified with 2 indexes - row_index, column_index
# as they are again next to each other we can get them easily by calculating the index
# in O(1) constant time complexity 


# indexes are also known as "keys"

"""two types of arrays"""

static_array = "size of the array does not change"
dyanmic_array = "size of the array may change dynamically" #basically the array might change

#more complex data structures rely heavily on arrays because of random indexing - 
# O(1) access of items with known indexes quickly 
# stack, queues or dictionaries 
