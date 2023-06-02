""" Enumerate """
#with the help of enumerate function python is not only going to return the values or varaibles but also going to return it's indexes 

for index, value in enumerate(range(5)):
    print(str(index) + " " + str(value))


a = ["chait", "animal", "cow"]

for index, name in enumerate(a): 
    print(str(index) + " " + str(name))

    