"""Local and Global variables"""

#Global variables - these can be used throughout the whole code/program 
number = 12


def myfunction(): 

    #local variable, and can't be called outside of this function or it's not known outside this function as it's local.
    number = 12
    print(number)


myfunction()

#so this won't work 
"""print(number)"""


