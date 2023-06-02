"""init constructor"""

class person: 

    # this is the so-called constructor or the initialisation block
    # this self is a reference to the object of the person class 
    def __init__(self, name, age): 
        self.name = name # you can create variables using this constructor 
        self.age= age

    def show_name(self): 
        print("my name is %s and my age is %s" % (self.name, str(self.age)))  



# we used the constructor to inject the given values
p = person("kevin", 23) #created an object
p.show_name()   


# we can also use keyword arguments just like functions 


class person: 

    # this is the so-called constructor or the initialisation block
    # this self is a reference to the object of the person class 
    def __init__(self, name, age): 
        self.name = name # you can create variables using this constructor 
        self.age= age

    def show_name(self): 
        print("my name is %s and my age is %s" % (self.name, str(self.age)))  



# we used the constructor to inject the given values
p = person(name="kevin", age=23) #created an object
p.show_name()   

# we can also use default values just like function


class person: 

    # this is the so-called constructor or the initialisation block
    # this self is a reference to the object of the person class 
    def __init__(self, name="chaitanya", age=43): # so you assign the default values here 
        self.name = name # you can create variables using this constructor 
        self.age= age

    def show_name(self): 
        print("my name is %s and my age is %s" % (self.name, str(self.age)))  



# we used the constructor to inject the given values
p = person() #created an object
p.show_name()   























