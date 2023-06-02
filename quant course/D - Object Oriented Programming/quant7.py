# method override 

class user:

    #initialisation block
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 

    def show_user(self): 
        print("The user is %s and the age of the user is %s " % (self.name, self.age))

    # if we create a show_info function here 
    
    def show_info(self): 
        print("this is from parent class")

class FacebookUser(user): 

    #super keyword is going to call the parent class
    def __init__(self, name, age):
        super().__init__(name, age) 

    # If we create the same show_info() function in the child class 
    def show_info(self): 
        print("this is from child class")

#defining the object
user1 = FacebookUser('Chaitanya Awasthi', 16)
user1.show_user()
print(user1.show_info())  # it's gonna output :- this is from a child class and it's gonna ignore the 
# parent class as the object is initialised in the facebookuser()