#Saving and loading numpy ARRAYS
#ndarray objects can be saved to and loaded from the disk
#files using IO function np.save('fname',ndarray) ,
#np.load('filename',array)

import numpy as np
x=np.arange(5)
print('x is',x)
print('saving file...')
np.save('myfile.npy',x)
# to load file and read with .npy extension

x_=np.load('myfile.npy')
print('loading')
print(x_)

#savetxt and loadtxt helps to save as .txt files

a=np.array([1,2,3,4])
np.savetxt('out.txt',a)
b=np.loadtxt('out.txt')
print(b)

# to check the datatype of the NumPy
ints=np.ones(shape=[2,2],dtype=np.uint16)
print(ints)
print(np.issubdtype(ints.dtype,np.integer))

print(np.float.mro())

print('\n\n-----------------------------------------\n\n')
#concatenating and splitting ARRAYS
arr1 = np.arange(15).reshape((3,5))
#arr1= arr1.reshape((3,5))
print('\n arr1 is \n',arr1)

arr2= np.arange(10,25).reshape(3,5)
print('\n arr2 is \n',arr2)

b= np.concatenate([arr1,arr2],axis=0)
print(' vertical after concat \n',b)

c= np.concatenate([arr1,arr2],axis=1)
print(' vertical after concat \n',c)

print('\n\n---------------------split-----------------\n\n')
