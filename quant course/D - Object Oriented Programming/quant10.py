# I can import another python file and use it's functions and variables 
import quant9 
quant9.fib(10)


# we can also use the from function and import the function "from" the file 
from quant9 import fib as f # we can also rename fib as f
f(19)


# we can also import variables from the other file 
from quant9 import user_preference as up
print(up["username"]) 

import collections # this means that there is a modular in python which consists of source code 


