"""diff b/w class variable and object variable"""

class person: 

    # CLASS VARIABLE
    # these variables and values are shared by all the objects in the given class 
    # so if i define a variable here before the constructor 
    gender = "male" # this 'gender' will be shared by all the objects below in this case (p, p1)
  
    def __init__(self, name, age): 
        # object/object variables : 
        # these variables are totally owned by the given object below. The values of these objects 
        # {self.name, self.age} : can differ depending on the objects
        self.name = name 
        self.age= age

    def show_name(self): 
        print("my name is %s and my age is %s" % (self.name, str(self.age)))  



p = person(name="kevin", age=23) 
p1 = person(name="hello", age=45)
p.show_name()   


class car: 

    color = "black"

    def __init__(self, brand, year): 
        # you do self.brand = brand and self.year because you allocate these variable to perform as object variables 
        # relating the class car to the variables with self.variable = variable
        self.brand = brand
        self.year = year

    # defining getters

    def get_brand(self): 
        return self.brand
    
    def get_year(self): 
        return self.year
    
# creating an object 

car1 = car("ferrari", 2000)
print(car1.get_brand())
print(car1.get_year())

