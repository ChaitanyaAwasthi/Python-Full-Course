""" list comprehension : allows us to create a new list based on existing values of another list"""

numbers = [1, -5, 0, 100, 10, 65, 34]

new_list = []

for num in numbers: 
    if num%2 == 0: 
        new_list.append(num)


print(new_list)


""" or we can use the "list comprehension approach" """

numbers = [1, -5, 0, 100, 10, 65, 34, 10]

new_numbers = [num for num in numbers if num % 2 ==0] # this just crunches out the condition in the loop itself. 

print(new_numbers)


names = ["chaitanya", "john", "mark"]
new_name = []

for name in names: 
    if names.startswith("A"): 
        new_name.append(name)

# by using the list comprehension method


names = ["chaitanya", "john", "mark"]
new_name = [name for name in names if name.startswith("A")]

new_name = [name for name in names if len(name) == 4]


""" why is python's array - list not considered a real array"""

"""Certainly! In Python, when you create a list and add elements to it, the underlying memory allocation is quite different from traditional arrays found in some other programming languages.

In a traditional array, elements are stored in contiguous memory locations. For example, if you have an array of integers [1, 2, 3, 4], the memory would be allocated as follows:

Memory Location	Value
1000	1
1004	2
1008	3
1012	4
In this case, each integer takes up 4 bytes of memory, and the memory addresses are consecutive.

However, in Python's list, the story is different. Instead of storing the actual elements in contiguous memory, a list contains a dynamic array of pointers to objects stored elsewhere in memory. These pointers point to the actual objects.

For example, if you have a Python list containing the same integers [1, 2, 3, 4], the memory allocation would look like this:

Memory Location	Value
2000	Pointer to 1000
2004	Pointer to 1004
2008	Pointer to 1008
2012	Pointer to 1012


Here, the memory addresses 2000, 2004, 2008, and 2012 contain references (pointers) to the memory addresses where the actual integer objects 1, 2, 3, and 4 are stored. 
    This level of indirection adds an overhead in terms of memory consumption and access time, as it requires additional memory to store the pointers and dereferencing them to access the actual objects.

This dynamic memory allocation scheme allows Python's list to be more flexible, as it can accommodate elements of different types and dynamically resize itself. 
However, it also introduces certain performance considerations compared to traditional arrays, especially when dealing with large datasets or performance-critical operations."""

#object is basically an entity in python which holds data



