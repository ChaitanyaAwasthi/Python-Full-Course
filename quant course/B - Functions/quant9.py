# global variable 
c = 10 



def test(): 

    global c #by this you are notifying python and you are changing the global variable inside the function
    c = 15


test()
print(c)


