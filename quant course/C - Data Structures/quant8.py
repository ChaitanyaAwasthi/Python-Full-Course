"""Mutability and Immutability"""

# immutable objects --- numbers, floating numbers, booleans, tuples

x = 5 
print(id(x)) # id function is used to output the memory location of the given object

x += 1 # if we increment x by 1
print(id(x))

# memory location of the variable[x]
140714632930216 # id of x 
140714632930248 # id of (x+1)

# as you can see that python creates a new memory location for the variable x, it's just python is creating a brand new variable...

# Mutable Objects --- lists, sets, dicts --- reason is just because it's more efficient

list1 = [1, 3, 4, 5]
print(id(list1))
list1[0] == 5
print(id(list1))

# memory location of the list
1888366248960
1888366248960 
# as you can see both are same, hence proving that lists are mutable objects




