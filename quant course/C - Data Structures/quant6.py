def is_prime(x):
 
    if x < 0:
        return False
    if x == 1:
        return False
    if x == 2:
        return True
 
    for num in range(2, x):
        if x % num == 0:
            return False
 
    return True 


# list comprehension

def is_prime(x):
 
    if x < 0:
        return False
    if x == 1:
        return False
    if x == 2:
        return True
 
    for num in range(2, x):
        if x % num == 0:
            return False
 
    return True
 
 
numbers = [1, 5, 43, 55, 76, 100, 123, 11, 2, -5, 87, 99]
 
primes = [num for num in numbers if is_prime(num)] # so in this we use the function above is_prime()
 
print(primes)

import time
 
nums = []
 
# start time in seconds - we will measure the running time of operations
start = time.time()
 
# let's insert 100k items at the end of the list - fast operation
for i in range(100000):
    nums.append(i)
 
print('Inserting at the end - time taken: %s' % (time.time() - start))
 
# re-initialize time
start = time.time()
 
# insert 100k items at the beginning of the list - index 0
for i in range(100000):
    nums.insert(0, i) # by using (0, i) you are inserting i at 0 index by saying 0 

# takes a lot of time because we have to shift the items !!!
print('Inserting at the beginning - time taken: %s' % (time.time() - start)) 

