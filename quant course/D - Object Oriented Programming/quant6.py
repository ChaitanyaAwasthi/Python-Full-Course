# inheritance
class user:

    #initialisation block
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 

    def show_user(self): 
        print("The user is %s and the age of the user is %s " % (self.name, self.age))

class FacebookUser(user): 

    #super keyword is going to call the parent class
    def __init__(self, name, age):
        super().__init__(name, age) 

#defining the object
user1 = FacebookUser('Chaitanya Awasthi', 16)
user1.show_user()

