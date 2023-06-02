
# string representation of objects

class person: 

    def __init__(self, name, age): 
        self.name = name 
        self.age = age 

    def __str__(self): 
        return 'person with name : %s and age: %s' % (self.name, self.age)


p = person("hello", 23)
print(p) # if we print p then it's going to output that p is an object of the class person and it's going to output it's memory location as well. 


# we can use the __str__ special function to return the object with a string. If we printed the object : p without this special function, 
# -- then it would just print that it's an object and it's memory location 
# -- but if we use this speical function and return it with a string usually  return with the instance variable it becomes more convenient that we can print out the object
# -- and know which name and age it's associated to...
