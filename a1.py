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
n = 5000

# A, I will be using ints
rand = random.randint(0,n)
print(rand)

