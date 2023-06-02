# Abstraction and Polymorphism

# this is the parent class - or abstract superclass
class sortingalgorithm: 

    def sort(self): 
        pass


class insertion_sort(sortingalgorithm): 

    # function override 
    def sort(self): 
        print("insertion sort is running")


class selection_sort(sortingalgorithm): 

    # function override 
    def sort(self): 
        print("selection sort is running")

class quick_sort(sortingalgorithm): 

    # function override 
    def sort(self): 
        print("quick sort is running")

# we ask the user what sorting algorithm to use 
num = int(input("please select which sorting algorithm you would like to use : "))

# we also have to make a null object to equate it to another 
sortingalgorithm = None # this is how you create a null object

if num == 0: 
    sortingalgorithm  = quick_sort
elif num == 1: 
    sortingalgorithm = insertion_sort
elif num == 2: 
    sortingalgorithm = selection_sort

sortingalgorithm.sort() # sort was the function made in the first parent class1
