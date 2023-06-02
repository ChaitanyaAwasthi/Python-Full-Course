"""Yield Operator"""

#return - send a specific value (object) back to it's caller

#yield - can produce a sequence of values (objects), it can resume execution.

def producer():

    for num in range(0,10,1):
        if num % 2 == 0: 
            yield num # by using yield it does not stop it's iteration, if we used return instead of yield it would have stopped it's iteration. 

# this is the end of the function

for n in producer(): #in this we use a for loop for the function itself, as it states for a variable in the function producer() print the variables from the function so interesting omg
    print(n)

    