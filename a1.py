# In this assignment you will experiment with random variation over 
# discrete events.It will be very helpful to use the analytical results
#  and the experimental results to help verify the other iscorrect. 
#  If they do not align, you are probably doing something wrong 
#  (this is a very powerful and importantthing to do whenever working 
#  with real data)


# Auth: Justin Francis
# Created: 01/08/2020
# Ver: 0.1
# Mod:

## part 1, Birthday paradox
import random
import numpy as np
import matplotlib as plt

# A, I will be using ints
def randomCollision():
    k = 0
    n = 5000
    collisionArr = np.zeros(n,)
    while 1:
        rand = random.randint(0,n-1)
        if collisionArr[rand] == 1:
            break
        collisionArr[rand] = 1
        k += 1
    return k


print('part A, k: ', randomCollision())

# B, 
m = 300
collisionResults = np.zeros(m,)

for i in range(m):
    collisionResults[i] = randomCollision()

