"""strings"""

# strings are one-dimensional arrays 
"""In Python, a character is essentially a string of length 1.
 there are no characters in python - characters are strings with a single letter ; """



 # we are able to acquire the given letter with indexes and index starts with [0]
 # we can get last letter with -ve indexes 

name = "chaitanya"
print(name[0])
print(name[-1])


"""you can create a range to acquires various indexes as well"""

print(name[0:2])

"""Strings are considered one-dimensional arrays because they represent a linear sequence of characters.
 Each character in a string is stored in a consecutive memory location, forming a contiguous block of memory.

In contrast, two-dimensional arrays are used to represent tabular data or matrices with rows and columns. They have multiple dimensions and require two indices to access individual elements. 
Two-dimensional arrays are useful for representing grids, tables, or matrices where data is organized in rows and columns."""



#we can only concatenate str with str and not int, to solve this problem we use the formate f(x)

text = 'hello i would like a piece of your pie {}'
num = 35

result = text.format(num)
print(result)





