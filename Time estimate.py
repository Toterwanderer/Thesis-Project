import numpy as np
import math

sum=0
for i in range(21):
    sum += i**2*(math.comb(20,i))
print(sum)