"""Break and Continue for Loops"""

# Break - we can stop the given loop before it has looped through all the items 
# Continue - we can skip (stop) the actual iteration of a loop and continue with the next iteration

"""Break Statement"""

counter = 0

while counter < 10:
    if counter == 5: 
        break
    print(counter)
    counter += 1



while True: 
    if counter == 100: 
        print(counter)
        counter += 1


"""Continue Statement"""

for number in range(1, 10 , 1): 
    if number == 5: 
        continue 

    print(number)
#continue means don't iterate 5 in this case and continue