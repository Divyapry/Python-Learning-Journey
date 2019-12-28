import numpy as np
arr = np.arange(15).reshape(3,5)
print(arr)
print("\n 1. now printing the transpose of the arr ")
print(arr.T)
print("\n 1.1 using the transpose function")
print(arr.transpose())

print ("\n 2. dot product of arrT and arr")
print(np.dot(arr.T,arr))

# transpose() is better as for higher dimensional arrays,
#it will accept a tuple of axis numbers to permute the axes
