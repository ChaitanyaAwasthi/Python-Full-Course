

# we can store key-value pairs in a dictionary - hash f(x) takes the key in order to calc the index 


dict1 = { "name": "kevin-smith", "gender": "M", "age": 12}

print(dict1["name"])

# if we think of the hash function which is used on to the keys to use them as indexes 
# us writing print(dict1["name"]) would be the same as writing the index of it to find the value of the key

# key() is used to get all the keys associated with the dictionary 
for key in dict1.keys(): 
    print(key)



# what if we want to use for loop to get the values instead of keys (using the values() function)
for value in dict1.values(): 
    print(value)

# we can also use the items() function to call all the items in the given dictionary... they will be shown as tuples 
print(dict1.items())
output = """dict_items([('name', 'kevin-smith'), ('gender', 'M'), ('age', 12)])"""

# we can also concatenate keys and values 
for key, values in dict1.items(): 
    print(key + " " +  str(values)) # in items() we get them as paires ---> items
    # we do str(values) because we can't cancatenate keys and values together if they are of different data types 

# we can also also concatenate two values through the zip() function

for key, values in zip(dict1.keys(), dict1.values()): 
    print(key + " " + str(values))


# we can also change the value of keys by :- 

dict1["name"] = "hello"

# you can also use the dict() function

fun = dict(name="kevin", age=12)
print(fun) # if we use this then also it's the same, just that ":" is replaced by "=" and you don't need "" in keys

"""we can also delete key:value pairs by using the del() function"""
del fun["name"]


#what if you wanna append a new key:value pair 

fun["color"] = "purple" # color is the key, purple is the value
print(fun)
print(len(fun))

"""the values can be written as dictionaries as well, i like to call it sub-dict"""

fun4 = { "name": {"first_name" : "chaitu", "last_name" : "awasthi"}, "gender": "M", "age": 12}
print(fun4["name"])
print(fun4["name"]["first_name"]) # this is like a directary i would say, it tells python from the name go tell me the first name






