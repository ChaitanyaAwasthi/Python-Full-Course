"""Fibonacci Numbers"""

# The Fibonacci sequence is a sequence in which each number is the sum of the two preceding ones

a, b = 0, 1

while a < 100: 
    print(str(a) + " " + str(b))
    a, b = b, a + b
  

"""The value of a is assigned the current value of b, and the value of b is assigned the sum of the current values of a and b"""




#construct with for loop 

a, b = 0, 1

for i in range(1, 10): 
    print(a)
    a, b = b, a+b


