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

### part 2, Coupon Collector
import numpy as np 
import random
import matplotlib.pyplot as plt
from collections import Counter
import time

n = 300
def fillRange(n):
    randDic = dict()
    k = 0
    while 1:
        rand = random.randint(0, n-1)
        randDic[rand] = 1
        k += 1
        if len(randDic) == n:
            break
    return k

# total = 0
# for i in range(100):
#     total += fillRange(300)
# print('k: ', total/100)

## B
m = 400
def runTrials(n, m):
    kArr = np.zeros((m,))

    for i in range(m):
        kArr[i] = fillRange(n)

    return kArr

kArr = np.sort(runTrials(n,m))

# countArr = np.zeros((int(max(kArr)), int(min(kArr))))

# collisions = 0
# idx = 0
# for i in range(int(max(kArr)), int(min(kArr))):
#     while kArr[collisions] <= i:
#         if collisions < m-1:
#             collisions += 1
#         else: 
#             break
#     if collisions == 0:
#         countArr[idx] = 0
#     else:
#         countArr[idx] = collisions/m
#     idx += 1

# plt.figure(1)
# print(countArr)
# print(max(kArr), '\t', min(kArr))


#create hist
values, base = np.histogram(runTrials(n,m), bins=m)
#evaluate the cumulative
cumulative = np.cumsum(values)
# plot the cumulative function
plt.figure(1)
plt.title('Cumulative Density Funciton, Coupon Collector, Justin Francis')
plt.ylabel('Fraction of Experiemental Success')
plt.xlabel('Trials, k')
plt.plot(kArr, cumulative/m, 'o')
plt.show()

## C
empiricalEst = np.sum(runTrials(n,m))/m
print('Empirical Est: ', empiricalEst)

##D
# Describe how you implemented this experiment and how long it took 
# forn= 300andm= 400trials.Show a plot of the run time as you gradually 
# increase the parametersnandm. (For at least 3 fixed valuesofmbetween
# 400and5,000, plot the time as a function ofn.) You should be able to 
# reachn= 20,000andm= 5,000

# mArr = np.linspace(400, 5000, 3)
# nArr = np.linspace(300, 20000, 3)
# timeArr = np.zeros((len(mArr), len(nArr)))

# for i in range(len(mArr)):
#     for j in range(len(nArr)):
#         tStart = time.time()
#         runTrials(int(mArr[i]),int(nArr[j]))
#         tStop = time.time()
#         tElp = tStop - tStart
#         print(tElp)
#         timeArr[i, j] = tElp

# plt.figure(2)
# plt.title('Run Time, Coupon Collector, Justin Francis')
# plt.xlabel('Time, t[s]')
# plt.ylabel('Size of Range, n[number of elem]')
# # plt.hold()
# x = timeArr[0,:]
# y = nArr
# plt.plot(x,y, 'r', label='m = 300')
# plt.plot(timeArr[1,:],y, 'b', label='m = 400')
# plt.plot(timeArr[2,:],y, 'g', label='m = 500')
# plt.legend()
# plt.show()