import random
import numpy as np
r1 = np.random.randint(10,50,size = (10))
print(r1)
print("===================================================================")
r2 = np.random.randint(10,50, size = (4,5))
print(r2)

print("===================================================================")
R1 = [24,36,47,22,31,33,42,13,34,45]
Q1 = np.percentile(R1,25)
Q2 = np.percentile(R1,50)
Q3 = np.percentile(R1,75)
print(Q1)
print(Q2)
print(Q3)