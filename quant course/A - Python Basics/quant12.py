"""while loop"""
#IT KEEPS LOOPING WHILE A GIVEN CONDITION IS VALID 




name = "kevin"
StartingPoint = 0

while StartingPoint < len(name):
    print(name[StartingPoint])
    StartingPoint += 1
#we can also use the else statement, if the above condition is False then py executes the else statement 
else: 
    print("condition is False")



"""how do we count up to 10 using while loop"""

counter  = 0 

while counter  < 10: 
    print(counter)
    counter += 1
else:
    print("counter didn't work")



#Construct an application that calculates the average of the first 10 items - starting with 1. So [1,2,3,4,5,6,7,8,9,10] 

item_counter = 0
sum1 = 0
 
for item in range(1, 11):
    sum1 += item
    item_counter += 1
 
print('Average of the first 10 items (starting with 1) is: ' + str(sum1/item_counter))



