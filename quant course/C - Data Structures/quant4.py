"""list advanced operations"""

list1 = [1, 3, 45]

list1.append("hello")
print(list1)

# as lists are indexed, there can be same items in a list 

#we can also use negative indexes to access numbers from the last 
print(list1[-1])

print(list1[1:3]) #excluding 3, works just like strings as strings are just 1-dimensional arrays 

#we can also cancatenate lists 

list2 = [1, 3, 4]
list3 = [344, 5, 5.4]

print(list2 + list3)


"""extend function in lists"""

# we can also just append all the items of list 2 to list 1 by using the extend function just like this 

list2.extend(list3) #this extends/appends all the items from list 2 to list 1
print(list2)


# this list's built-in function

"""append() - used to add/append new item at the end of the list"""
list1.append("1")

"""copy() - can be used to copy a particular list and fork it on to another list or simply just paste"""
for_example = list1.copy() # this copies the list1 items and pastes it to for_example in this case 
print(for_example) # now by printing for_example, list1 items show up 

"""remove() - used to remove items """
list1.remove(3) # now this will remove 3 from the given list
print(list1)

"""pop() Like, remove(), pop() is also an in-built function used in Python for deleting the elements from the list. It removes the value based on the index. It takes the index/position of the element to be removed as its parameter. 
Passing the index is optional. If the index is specified, then it removes the element present at that particular position, else removes the last element of the list. The catch is it returns the removed element"""

#pop() uses index, without any parameter in pop(), it's O(1) but when specified parameter it's O(N)
list1.pop(2) # removes "hello" from list1
print(list1)

list1.reverse() #order of the item changes 

list_names = ["ynna", "zevin", "chaitanya", "aoe"]
list_names.sort()
print(list_names) # result will be the list in alphabetical order omg


