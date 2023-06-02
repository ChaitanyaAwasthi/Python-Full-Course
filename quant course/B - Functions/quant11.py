"""__main__ function"""

"""In Python, the __name__ variable tells us the name of the script or module we are currently working with. 
By checking the value of __name__, we can know whether a script is being played with directly (as the main toy) or being brought into the game (used as a module)."""


"""In Python, the line if __name__ == "__main__" is a way to check if the current script is being executed directly (as the main script) or being imported as a module by another script."""

#the primary script you have all your functions and variables in, is known as the main file. But the file you are importing the module to is given by it's name itself 



def say_hello(): 
    print("hello")

if __name__ == '__main__':   #this sets the entry point for python # this makes sure that the code below it is only being run if it's the main module and not an imported one
    say_hello()
    

"""By setting an entry point, you are defining the initial code that will be executed and determining the behavior of your program when it is run. 
This is particularly useful when you have a script that can be used as a standalone program or imported as a module by other scripts."""
#python will know that this is the main file