import numpy as np
array = np.empty([3,3],dtype= 'int')
print('the empty array is \n ', array)
array[1,:3] = np.zeros(shape=[1,3],dtype='int')
print('after zero function \n', array)
array[2,:3] = np.ones(shape=[1,3],dtype='int')
print('after ones function \n', array)

# accessing array elements in ndarray
print('\n \n \n')
x = np.arange(50,80)
print(x)
print('x[5]=',x[5])
# using slice object x[start:stop:step]
print('\n', x[3:10:2])
# using tuple of slice objects
print('\n', x.size)

print('\n', x[28:])
print('\n ---------------------TASK -2-------------------------')

narray = np.arange(10)
print(narray)
print('slicing to print 5th,7th,9th elements \n')
print(narray[5:10:2])
print(narray[0:10:2])

print('\n-----------------------advance indexing--------------')

x=np.array([[28,43],[22,11]])
print(x)
x_= x[[0,1,0],[1,1,0]]
print('\n', x_,'\n')

y = np.array([[0,1,2],
             [3,4,5],
             [6,7,8]])
print(y)

y_= np.array([[y[0,0],y[0,1],
             [y[2,2],y[2,2]]]])

print('\n new \n' ,y_)
print(y_.ndim)

print("---------------------reshaping arrays-------------------")

a = np.array([[0,1],[2,3],[4,5]])
print('original array:')
print(a,'\n',a.shape)

a_ = a.reshape(2,3)
print('reshape will create a new instance os array \n',a_)

print('--------------------resize-----------------------------')

a=np.array([1,2,3,4,5])
print('original \n',a)
a.resize(2,3)
print('after resize \n',a)
