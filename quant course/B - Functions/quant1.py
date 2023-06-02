"""functions"""


def Given_Name(name):
    print("The name of the person is : " + name)

Given_Name("Chaitanya")

# diff b/w parameters and arguments 
"""in this case name is the parameter and "chaitanya" is the argument"""

#we can also define a local variable

def Given_Name1(name1):
    #local variable 
    age = 10 
    print("The name of the person is : " + name1)
    print("the age of the person is : {}".format(age))
Given_Name1("Chaitanya")

#double parameters
def Given_Name1(name1, age):
    print("The name of the person is : " + name1)
    print("the age of the person is : {}".format(age))
Given_Name1("Chaitanya", 12)

#we want to define a function without a body
#python does not have anti-functions


def x(first, second): 
    pass
"""python ignores this function due to the pass keyword"""

