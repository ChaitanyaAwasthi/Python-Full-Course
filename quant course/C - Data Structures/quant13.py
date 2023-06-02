"""sorting"""

nums = [34, 45, 23, 5, 6, 2, 54, -1]

# sorted function always returns a list // ascending order
print(sorted(nums))

# descending order ? 

descending_order = (sorted(nums, reverse=True))
ascending_order = (sorted(nums, reverse=False))

print(descending_order, ascending_order)

names = ["adam", "chaitanya", "joe", "daniel", "michael"]
# alphabetical order 
ordered_list = sorted(names)
print(ordered_list)

# if you wanna reverse the alphabetical order of the list
negative_ordered_list = sorted(names, reverse=True)
print(negative_ordered_list) 

# sorted function has the key parameter - we can define the logic behind sorting 
# let's sort names based on the length of the strings 


def sorted_logic(x): 
    return len(x)


text = ["this", "t", "djirfjdnrf", "drjfdjxk"]
text = sorted(text, key=sorted_logic) # in this we took the key which is also the logic as the function
# we defined before...

# we can also directly define the len logic in the parameter as well 

text = sorted(text, key=len, reverse=True)
print(text)
print(text)


# what if we wanna sort dictionaries 

# defining the key

def sorter(x): 
    return x[1]
    
# so when we say sort the dictionary where the logic is return x[1], that means sort according to the 
# value, and when you say return x[0] that menas sort according to the key

people = {"chaitanya" : 34, "adam" : 24, "josh" : 23}
# in dictionaries, indexing works like 
""" chaitanyas, adam, josh: [0]
    34, 24, 23            : [1]
    """

result = sorted(people.items(), key=sorter)
print(result)



















