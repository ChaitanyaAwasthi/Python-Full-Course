"""NESTED LOOPS"""

#loops inside of loop 


for outer in range(5):
    for inner in range(3):
        print("outer: " + str(outer) + " " + "inner: " + str(inner))

"""
outer: 0 inner: 0
outer: 0 inner: 1
outer: 0 inner: 2
outer: 1 inner: 0
outer: 1 inner: 1
outer: 1 inner: 2
outer: 2 inner: 0
outer: 2 inner: 1
outer: 2 inner: 2
outer: 3 inner: 0
outer: 3 inner: 1
outer: 3 inner: 2
outer: 4 inner: 0
outer: 4 inner: 1
outer: 4 inner: 2

#For each iteration of the outer loop, the inner loop is executed in its entirety. It iterates over the elements of the inner sequence
#The inner loop completes its iterations, and the control goes back to the outer loop. It moves on to the next element in the outer sequence, and the process repeats.
#So basically for every iteration of the outer loop, the inner loop is done fully and then when the inner loop finishes the outer loop is iterated, this is done until the outer
loop is finsihed
"""