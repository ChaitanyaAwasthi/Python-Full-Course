#this is the class so the blueprint 
# encapsulation - it is a fundamental feature of OOP
# we are going to group functions and variables 
class person:
     # you can define a variable  
    name ="chaitanya"
     # you can also define a function
    def show_name(self): # this self is going to reference to the person object 
        print("my name is : " + self.name) # self.name means we would like to access the variable associated with the person
# p : is the object
p = person() # why implement this line of the code, because then we can access the variable with this object
print(p.name)
p.show_name() # we can also call the function with the help of the object 'p'


 
