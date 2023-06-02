"""Tuples"""

# they are very similar to lists but the only difference is that tuples can't be changed
# tuples are immutable objects 
# list - [], tuple - ()

my_tuple = ("joe", "heLLo", "myname", 20, False, "hello this is my tuple")

"""my_typle.append # this can't be done 
my_typle[0] == "hello" # this can't be done """


for names in my_tuple: 
    print(names)

# what if we wanna define a tuple with only one single item 
# if we do that the conventional way that's gonna become a string 

one_item_tuple = ("hello") # that's like defining a normal variable as a str
one_item_tuple = ("hello", ) # this is how you define a single-item tuple


# tuple has random indexing 

