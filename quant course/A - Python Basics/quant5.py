
x = '0123456789'


"""string slicing"""

print(x[0:7]) 



"""it's fine if you don't define the starting initiation as python automatically inteprets that it's 0 if ofc you want 0"""


"""the output includes the starter but does not include the end number so in this case includes 0 but does not include 7"""
print(x[:7])

""" if you just include a ':' then python will intepret the whole string which is given """
print(x[:]) == print(x[:10])

"""we can define the step size"""
print(x[0:10:2]) #output - 02468
# the alst initiation is the step size which means in this case the program will just "2" places and return the value according to that

#if we use -ve value as step size then it will go from right to left
print(x[0:10:-1])

#this will reverse the string as it will take 0: maximum char: and -1 as step size which will reverse the 1D Array
print(x[::-1])

