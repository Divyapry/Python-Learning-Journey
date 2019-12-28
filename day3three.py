# flatten function collapses the array into one DIMENSIONAL

import numpy as np
x= np.ones(shape=[3,4],dtype='int')
print('original array \n', x)
print(x.shape,'\n')

x_=x.flatten()
print('new flattened array \n', x_)
print('\n shape is', x_.shape)

# ravel is also a function which does same operation as flatten
#but is more faster than the flatten function

y=np.ones((3,4,5))
y_=np.ones((4,5))
print('y creates 3 subarrays each with 4 rows and 5 columns\n ',y)
print('diff y_ is\n', y_)

#now performing the ravel operation on y
y_r = y.ravel()
print('after ravel', y_r,'\n','y_r.shape')

f_r=y.flatten()
print('\n \n', f_r)


#Differene between ravel and flatten is that
# 1) ravel() this function returns a view or reference of original array.Hence,
#if we modify the array we can notice that value of the original array also changes
# 2) flatten() returns the copy of the array. Hence, any modifications is notat
# reflected in the originial arrays.
# So which is faster?
# ravel is faster as it does not occupy any memory.
