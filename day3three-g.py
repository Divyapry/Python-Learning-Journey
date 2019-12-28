#using transpose
import numpy as np
x=np.ones((3,4))
print('original array:\n',x)
print('\n',x.shape)

x_=x.T
print('transpose is \n ', x_)

#Inverse of an arrays A^-1 = 1/ad-bc [d -b]
#                                    [-c a]

import numpy as np
x = np.array([[4,7],[2,6]])
y = np.linalg.inv(x)
print ('original matrix is \n',x)
print ('\n inverse of the matrix using linalg.inv is \n', y)
print( '\n dot product of inverse * orginal should give identity matrix \n')
print(np.dot(x,y))

#dot product in numpy in calculated using np.dot(x,y) whereas cross product
# or element by element multiplication is using X*Y

# numpy.stack function is used to stach the single array wither vertically
# or horizontally using functions np.hstack or np.vstack
print("\n-----------------------------------------------------------------\n")
import numpy as np
a = np.array([[1,2],[3,4]])
print('first array \n',a)
b = np.array([[5,6],[7,8]])
print('\n second array \n',b)
print('\n-----horizontal stacking of the arrays----------\n')
c=np.hstack((a,b))
print(c)

x=np.arange(3,30,3)
print('x:\n ',x)
y=np.array(['a','b','c'])
print('y:\n',y)
z=np.hstack((x,y))
print('\n\n hstack is\n',z)

print('\n---------------------------vertical stacking---------------\n')
print('\n a is \n',a)
print('\n b is \n',b)
d=np.vstack((a,b))
print('\n vertical stack is \n',d)
e=np.hstack((a,b))
print('\n horizontal stack is \n',e)
