# 1) NUMPY ARE N-DIMENSIONAL ARRAYS CONTAINING HOMOGENOUS ITEMS.
#2) EVERY NUMPY HAS SHAPE AND DATA TYPE ASSOCIATED WITH IT.
# 3) SHAPE AND DATATYPE CAN BE FOUND USING THE ATTRIBUTES.
import numpy as np
x= np.array([[1,2],[3,4]])
print('array is : \n', x)
print('1) shape of array can be determined using - x.shape which gives : ' ,x.shape)
print('2) data type of array is strored n dtype attribute', x.dtype)
print('3) dimension of array is', x.ndim)
print('4) object type of array is ', type(x))
print('5) size of array is ', x.size)
print ('\n TO FIND SIZE OF EACH ELEMENT OF ARRAY')
print(x.itemsize)
print('total bytes consumed', x.nbytes)

# 4) to create an uninialized numpy ARRAY
x=np.empty( shape=[2,2],dtype = int)
print('\n', x)
