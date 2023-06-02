"""Array Operations"""

Adding_Items = """ we can insert new items at the end of the data structure
till the data structure is full"""

# now the question arises "What if the data structure becomes full ? "

"""
1) first of all you have to allocate large chunk of memory to the ram, 
usually 2x the array size
2) have to copy item one-by-one
3) #because of this one-by-one operation the resizing of an array take linear running
time complexity O(N)- bottleneck operation"""

# There is a huge trade off
# Memory and Running Time Trade-OFF !!
"""either start with a small sized array, that would not waste memory but 
would have to resize the array often with O(N) running time 

or allocate a huge array at the beginning itself, that would waste memory because
of the larger size but we do not have to bother with the resize operation :-
resulting to decreased time complexity from O(1) --> O(N) """


"""
Array Operations:- 

adding numbers to an arbitrary position - for example if we want to insert a new 
item at a given index example [2]. So the existing item in that index would increment 
to index[3] and so on. This follows a linear running time complexity O[N]"""

"""
Removing last item, we'll just remove the last item as it does not really affect 
the data structure as such"""

"""
Removing item from arbitrary position
problems: - we usually don't know the index of the item we wanna remove
2) after removing we have to deal with so called "holes" in the data structure

first we have to find the item in O(N) running time then remove the item in O(1)
and finally have to decrement or shift the other items in O(N)"""


"""Features of Arrays 

the best feature is the random access feature, we can access any arbitrary item if 
we know the index of the item
use arrays if you wanna manipulate the last item of the structure or access items with
known indexes"""

"""Disadvantages 

1) we would have to know the number of items we want to store at compile-time
Not dynamic, if you wanna resize you have to resize it in O(N)
Python is an exception as we can store items with different Data-Types"""