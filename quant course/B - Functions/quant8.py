"""Recursion"""
###

"""In python it's possible for a function to call itself, a function that calls 
 itself is said to be recursive..."""

 #every problem with can be solved with iteration can be solved with recursion
 # iteration occurs with while loop, for loop

"""iterative method"""

def sum_iterative(n): 

    #defining local variable 
    total = 0 



    for num in range(0, n + 1, 1): 
        #if we use (0, n, 1) // n will be exclusive
        #so we have to use n  + 1 to include the exclusive digit
        #iteration
        total += 1 

    return total 


#with n it sums up every integer till the n defined which in this case is 10
define = sum_iterative(10)
print(define)


"""recursion method"""

def sum_recursion(n): 

    #defining the base case - where to stop the recursion...
    if n == 0: 
        return 0 
    
    return n + sum_recursion(n-1)
print(sum_recursion)




def sum1(n): 

    #defining something i like to call an empty bowl as a local variable 
    bowl = 0 

    for num in range(n+1): 
        bowl += 1

    return bowl



def sum2(n):
    #if in this case we wanna find the sum till 5, we start from 5 which is opp to 
    #...iterative method

    if n==0:  #if the algorithm reaches 0 return 0 
        return 0 #return 0 
    else: #else
        return n + sum2(n-1) #
    
    """return n + sum2(n-1)
       return (n=5) =  5, sum2 -> means calling the function sum2 and now doing n-1 
       which is 4. [5 + 4] now the n is 4 then we take the function again n-1
       [5 + 4 + 3 + 2 + 1]"""
    #opposite of iterative method which was [1 + 2 + 3 + 4 + 5]

 

    
print(sum2(5))




#calculate factorial of a given integer 


def factorial(n):
    
    """n! = n*(n-1)!: 
    (n-1)! = (n-1)*(n-2)!"""

    if n==0: 
        return 1 #factorial of 0 == 1
    
    return n*factorial(n-1)

print(factorial(5))


"""Construct a recursive function that takes 2 parameters as 
input - a string and a given index ( of the text).
 The aim is to visit every character of the text 
 (from left to right - so starting with index 0) recursively.

Good luck!"""

def process(txt, i):
 
    # base case - when to terminate
    if i == len(txt):
        return #return with none
    else:
        print(txt[i], i)
        #so if i = 0, chaitanya[0] = c and the i keeps incrementing  
    return process(txt, i+1) #this restructures the function making it txt, and incrementing the index
 
 
  

print(process('chaitanya', 0))





    
    

    


    












