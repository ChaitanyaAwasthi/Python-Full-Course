# global variable 
c = 10 



def test(): 

    global c
    c = 15


test()
print(c)


