import numpy as np
arr= np.arange(32).reshape((8,4))
print(arr)

print("print elements at respective postion")
print(arr[[1,5,7,2],[0,3,1,2]])

print("to select one rectangular region of an array")
print(arr[[1,5,7,2]][:,[0,3,1,2]])

print("using np.ix_ function")
print( arr[np.ix_([1,5,7,2],[0,3,1,2])] )
