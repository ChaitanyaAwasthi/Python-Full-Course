
# The Aim of Encapsulation(data hiding) is to hide the implementation details from the users 
# Using Private variables is one form of encapsulation
# Private variables can be accessed from the given class exclusively (cannotbe accessed from outside)

##### There are no Real Private Variables #####

# in order to achieve that 
#  single underscore operator 
# a single _ underscore notifies the programmer that the given variable or function is private ( so should not be called from outside the class)
# a double __ underscore operator renames the varaibles: this is how pythonh handles private variables and it is called name mangling 


class person: 

    _color = "green" # this is not a pvt variable 

p = person()
print(p._color)
 

# with the help of name mangling (double__underscore method)


class person:

    __color = "green" # so with __ we can achieve "private variables"


p = person()

print(p._person__color)

# but this is not completely like a private variable....why ? 
