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


print('k: ', fillRange(n))

## B
m = 400 
kArr = np.zeros((m,))

for i in range(m):
    kArr[i] = fillRange(n)


#create hist
values, base = np.histogram(kArr, bins=40)
#evaluate the cumulative
cumulative = np.cumsum(values)
# plot the cumulative function
plt.title('Cumulative Density Funciton, Coupon Collector, Justin Francis')
plt.ylabel('Fraction of Experiemental Success')
plt.xlabel('Trials, k')
plt.plot(base[:-1], cumulative/m, 'o')
plt.show()

## C
empiricalEst = np.sum(kArr)/m
print('Empirical Est: ', empiricalEst)

##D
