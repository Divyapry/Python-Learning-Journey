import numpy as np
a = np.array([[1,2,4,7],[9,88,6,45],[9,76,3,4]])

y= np.where(a<=5)
print(y)

print(np.cumsum(a))

print('\n', np.unique(a))

print('\n',np.sort(a))

print('min element is',np.min(a))
print('max element is',np.max(a))
print('arg min element is',np.argmin(a))
print('arg max element is',np.argmax(a))


print('-----------------------------------------------------------')


from numpy import random
print(random.seed(8))
print('second time', random.seed(8))
print(random.rand(3))


print('\n using randit funtion')
print(random.randint(3,10,5))



from numpy.random import shuffle
np.random.seed(5)
c=np.arange(10)
print('Before shuffling: ',c)
shuffle(c)
print('after shuffling: ',c)

print('-----------------------')
print(np.random.seed(5))
