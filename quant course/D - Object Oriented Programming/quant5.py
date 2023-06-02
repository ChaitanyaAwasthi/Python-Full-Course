"""Inheritance in OOP"""

# inheritance allows us to define a class (child class or derived class) that inherits all the properties-
# - and functions from another class (parents class) 

# we can define a given variable with functions, variables, features only once in a class and then
# we can reuse this behavior in another class 


class algorithm: # parent class

    # class variable 
    general_message = "This has something to do with algorithms"


class sorting_Algorithm(algorithm): # child class 

    # class variable 
    sorting_message = "this is a sorting algorithm"
    
# this is because of inheritance 
sorting_Algorithm = sorting_Algorithm()
sorting_Algorithm.general_message # as you can see i can access general message from the algorithm 
# class by using sorting_algorithm.general_message
