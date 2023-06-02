"""how to return multiply variables"""

def operation(x): 

    if x % 2 == 0: 
        return True, 1
    else: 
        return False, -1
    
result = operation(10)
print(result[0])
print(result[1])


"""Python Programming Exercise

Construct a function that has 1 parameter - the x variable. 
If x is smaller than 0 then return with 0. Otherwise return with +1. (Note: there may be multiple return statements in a given function)"""


def exercise(x):

    if x < 0: 
        return 0
    else: 
        return 1

output = exercise(-10)
print(output)



