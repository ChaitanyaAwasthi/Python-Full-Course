

class person: 

    def __init__(self, name, age): 
        self.name = name 
        self.age = age 

    def __eq__(self, other): # the other object shows that another object is being compared to another object, "other" here is p2 as p1 is being compared to p2
        return self.age == other.age
    # so if we use p1==p2 it's only going to return True if the age instances are equal

# how to compare the objects
p1 = person("adam", 23)
p2 = person("joe", 23)

# we can override the standard functions
# __eq__ this is the built-in function to decide whether two objects are equal or not


print(p1==p2) # this is going to output True because we used the __eq__ special function



# what if instead of '==' we wanna use '<' to compare

class person: 

    def __init__(self, name, age): 
        self.name = name 
        self.age = age 

    def __gt__(self, other): # the other object shows that another object is being compared to another object, "other" here is p2 as p1 is being compared to p2
        return self.age > other.age
    # so if we use p1==p2 it's only going to return True if the age instances are equal

# how to compare the objects
p1 = person("adam", 23)
p2 = person("joe", 23)

# we can override the standard functions
# __eq__ this is the built-in function to decide whether two objects are equal or not


print(p1<p2) # this is going to output True because we used the __eq__ special function




# what if instead of '==' we wanna use '>' to compare

class person: 

    def __init__(self, name, age): 
        self.name = name 
        self.age = age 

    def __le__(self, other): # the other object shows that another object is being compared to another object, "other" here is p2 as p1 is being compared to p2
        return self.age < other.age
    # so if we use p1==p2 it's only going to return True if the age instances are equal

# how to compare the objects
p1 = person("adam", 23)
p2 = person("joe", 23)

# we can override the standard functions
# __eq__ this is the built-in function to decide whether two objects are equal or not


print(p1<p2) # this is going to output True because we used the __eq__ special function
