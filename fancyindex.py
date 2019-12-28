import numpy as np
arr = np.empty ((8,4))
for i in range(8):
    arr[i]=i
print(arr)

print("selecting the subset of rows in particular order")

print (arr[[2,4,6]])

print("if the -ve indices are used then rows are selected from the end.")

print(arr[[-1,-3,-2]])

print("array elements at respctv pos")
print(arr[[1,5,7,2],[0,3,1,2]])
