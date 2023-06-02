

num = input("Please, enter a number: ")
num = int(num)  #this will make sure that the ouput is an integer as it converts it 
print(type(num)) 


""" using various different conditional statements """

if num % 2 == 0: # % modular statement gives out the remainder 
    print("x")
elif num % 3 == 0: 
    print("y")
elif num % 5 == 0: 
    print("z")
else: 
    print("this number is not special at all")


"""we can use these elif statements to use if many times"""

"""if py finds one statement true from the start through it's run-through it's gonna stop the program"""

#concatenate conditional statements 
if num % 2 or num % 5 == 0: #either one of the statement needs to be true
    print("yes")
elif num % 2 and num % 5 == 0:  #both of the statements needs to be true 
    print("yes!")


#practice exercise 

intInput = input("Please, put in your number: ") 
intInput = int(intInput)
if intInput < 0:
    print("given integer is smaller than zero")
elif intInput >= 0 and intInput <= 10: 
    print("the given integer is within the range [0,10]")
else: 
    print("int is greater than 10")


