import numpy as np
list = [1,2,3,4]
array = np.array(list)

print(array)

print(array*40)
print(array+10)

list2 = [[1,2,3],[4,5,6],[7,0,9]]
arr2d = np.array(list2, dtype= 'int')
print(arr2d)
#convert int to float
arr2d_float = arr2d.astype('float')
print(arr2d_float)
#convert int to str datatype
arr2d_str = arr2d.astype('str')
print(arr2d_str)
# create a boolean array
arr2d_b = arr2d.astype('bool')
print(arr2d_b)

#create an object array to hold numbers as well as strings
arrd_obj = np.array([1,'a'],dtype='object')
print(arrd_obj)

#to convert the array back to list
arrd_obj = arrd_obj.tolist()
arrd_obj.append('bb')
print(arrd_obj)

#shape, type, size , dimension
list3 = [[1,2,3,12],[4,5,6,9],[7,0,9,2]]
arr3d = np.array(list3, dtype= 'float')
print(arr3d)
print('Shape: ',arr3d.shape)
print('type: ', arr3d.dtype)
print('size: ', arr3d.size)
print( 'dimensions: ',arr3d.ndim)

#extract first 2 rows and 2 columns
print(arr3d[:2,:2])

#boolean array by applying condition to each element
b = arr3d > 2
print(b)
print(arr3d[b])

#to reverse the rows and the whole array
print("\n REVSERSE THE ROWS AND ARRAY \n")
print(arr3d)
print('reverse array:\n',arr3d[::-1])
print('reverse row & columns:\n', arr3d[::-1,::-1])

#represent missing values and infinite
"""list4 = [[1,2,3],[4,5,6,9],[7,9,2]]
arr4d = np.array(list4, dtype= 'float')
print(arr4d)
print(arr4d.ndim)"""
arryd[2,3] = np.nan
print('nan function:\n' , arryd)
