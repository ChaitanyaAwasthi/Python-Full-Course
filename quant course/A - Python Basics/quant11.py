"""loops"""

"""A loop is a programming structure that repeats a sequence of instructions until a specific condition is met"""

#the algorithm loops until a specific condition is met. </p>

"""For Loop:- defines the start and end point as well as the increment for each iteration"""

for number in range(5):
    print(number)
#this outputs 0,1,2,3,4

for number1 in range(1, 5, 2):
    print(number1)

#5 would not be included...

#the first parameter in this case 1 is the starting point 
#the second is the end point which is exclusive in nature
#the third is the increment or the step size which in this case is two 

name = "chaitanya"
for letter in name: 
    print(letter)
# we can use else statement to run a given operation right after finishing the for loop
else: 
    print("loop was executed")

#letter is the variable in this case and number, number 1 was variables in the given term whether it's in int or str
