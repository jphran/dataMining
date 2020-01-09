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

### part 1, Birthday paradox
import random
import numpy as np
import matplotlib.pyplot as plt
import time

## A, I will be using ints
n = 5000
def randomCollision(n):
    k = 0
    collisionArr = np.zeros(n,)
    while 1:
        rand = random.randint(0,n-1)
        if collisionArr[rand] == 1:
            break
        collisionArr[rand] = 1
        k += 1
    return k


print('part A, k: ', randomCollision(n))

## B, 
m = 300


#collect data and time
def produceCollisionResults(n,m):
    collisionResults = np.zeros(m,)
    for i in range(m):
        collisionResults[i] = randomCollision(n)
    return collisionResults

collisionResults = produceCollisionResults(n,m)

#manipulate data to plot cumulative density
collisionResults = np.sort(collisionResults)
fractions = np.zeros(m)

collisions = 0
for i in range(m):
    while collisionResults[collisions] <= i:
        if collisions < 299:
            collisions += 1
        else: 
            break
    if collisions == 0:
        fractions[i] = 0
    else:
        fractions[i] = collisions/m

#plot
plt.title('Cumulative Density Plot of Random Collisions, Justin Francis')
plt.ylabel('Fraction of Experiment Collisions After k Trials')
plt.xlabel('Trials, k')
plt.plot(collisionResults, fractions, 'o')
plt.show()

## C 
print('expected number of k for a collision:', np.sum(collisionResults)/m)

## D
# mArr = np.linspace(300,10000, 3)
# nArr = np.linspace(5000, 1e6, 3)
# nTime = np.zeros((len(mArr),len(nArr)))

# nidx = 0
# for nCurr in nArr:
#     midx = 0
#     for mCurr in mArr:
#         tStart = time.time()
#         produceCollisionResults(int(nCurr),int(mCurr)) 
#         tStop = time.time()
#         nTime[midx,nidx] = tStop - tStart
#         midx += 1
#     nidx += 1

# print(nTime)

