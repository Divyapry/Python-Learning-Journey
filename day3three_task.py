import numpy as np

x= np.array([[42,22,12],[44,53,66]])
print('array x is \n', x)
x_= x.reshape((3,2))
x_.resize((2,3))
print('\nrr ',x_)

#reshape creates new instance of array while resize creates only view or
#reference of an arrays
b=x.flatten()
print(b)

g=x.T
print ('transpose is \n',g)

h=np.hstack(x)
print(h)

v=np.vstack(x)
print(v)
