# positional parameters and arguments - the order does matter
def Given_Name1(name1, age):
    print("The name of the person is : " + name1)
    print("the age of the person is : {}".format(age))
Given_Name1("Chaitanya", 12) 



#what if we had multiple names 

def Given_name2(*names): #with *args you can store multiple arguments in a parameters 

    print(names[0])
    print(names[1])
    print(names[2])

Given_name2("chaitanya", "rohan", "John")
#the parameter is going to store these three values )

"""what if you want the output to show the names on by one in different lines"""

def names(*name): 
    for index in range(len(name)): 
        print(name[index])

"""Defining Default Values"""

def default(name="chaitanya"):
 
 default() #as there is no argument given, python will use the default value given above name="chaitanya"...
#and if an argument is given and so is the default value, the argument will be used...

"""keyword argument""" ""
#why use keyword argument and not regular calling of a f(x), becuase in keyword argument order does not matter
def name(names, age):
   
   print("the name of the person is : " + name)
   print("the age of the person is : {}".format(age))

name(names="chaitu", age=12)

"""what if we don't know how many keyword arguments there are gonna be in a compiled manner"""

#for this we use - **

def info(**params): 
   print(params[name])
   
   info(name="chaitu", age=12, gender="male", interest="finance")





