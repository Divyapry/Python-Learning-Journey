import numpy as np
from numpy import random

arr = np.arange(10)
print(arr)

"""USING UNARY FUNCTIONS"""

print(np.sqrt(arr))
print(np.exp(arr))

a1= np.array([[1,22,3,14]])
b1= np.array([[5,6,2,38]])

print("using maximum function")
print(np.maximum(a1,b1))

print("using add function")
print(np.add(a1,b1))

print("using modf function")#modf seprates int and decimal part
print(np.modf(11.234))
print(np.modf(12))

arr = random.randn(7)
print(arr*5)
print(np.modf(arr))
