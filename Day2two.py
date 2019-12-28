import numpy as np
#1) to create unintialized numpy array
x = np.empty(shape=[3,3],dtype=int)
print('empty array using n.empty will print:\n', x)

# 2) to create an nd array with all zeros we use function
# np.zeros (shape=(x,k),dtype='float', order='c'or 'f') order atribute is
# optional here this is used to determine whether to store multidimesional
# data in C or Fortran contiguous memory

y = np.zeros( shape = [2,2], dtype ='float', order='C')
print('zero array: \n', y)

#3) to print an array full of ones only

z= np.ones( shape=[2,3], dtype='int', order='C')
print('ones array is :\n',z)

#5) to create numpy array having evenly spaced values with given range

a = np.arange(start=10,stop=100,step=5,dtype=int)
print('using arange:\n', a)

print('evenly spaced:\n', np.linspace(1,5,1))
