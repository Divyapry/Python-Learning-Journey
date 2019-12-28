#np where is like asking where the array is and providing entries to satisfy
#the condition
import numpy as np
x = np.arange(10,100,10)
print(x)
y = np.where(x>70)
print('y value is',y)
print('x>70 :\t', x>70)
print('output with x:',x[x>70])
print('output with np.where:',np.where(x>70))

random=np.array(['huwhdw',34,'jdnwkd'])
print(random.nbytes)

#np.cumsum this function basically returns the cummulative sum of the elements
#alnog a given axis
import numpy as np
x1=np.arange(5)
print('x1 is:\t',x1)
print('np.cumsum(x1):',np.cumsum(x1))

x2=np.array(['a','b','c','d'])
print('\n \n x2 \t:',x2)
try:
    print('np.cumsum(x2):',np.cumsum(x2))
except Exception as e:
    print ('np.cumsum(x2):Exception->',e)


#np.unique unique elements of an array
a = np.array(['hyd','mum','pune','kol','hyd'])
print(np.unique(a))
print(len(np.unique(a)))

array = np.array([[1,1,1,0,0,0],
                  [0,1,1,1,0,0],
                  [0,1,1,1,0,0],
                  [1,1,1,0,0,0],
                  [1,1,1,1,1,1]])
print('array: \n',array)
unique_rows = np.unique(array)
print('\n when axis attribute is not given \n:', unique_rows)
unique_rows1 = np.unique(array, axis=0)
print('\n when axis attribute is given as 0 it prints unique rows \n:', unique_rows1)
unique_rows2 = np.unique(array, axis=1)
print('\n when axis attribute is given as 1 it gives unique columns\n:', unique_rows2)
