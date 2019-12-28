import numpy as np

print(np.__version__)
np.show_config()

print("\n 3. create null vector of size 10?")

print(np.zeros(10))

arr = np.arange(10,49)
print(arr)

print("2. REVERSING THE VECTOR")
brr = np.zeros(39)
j=-1
for i in range(39):
    brr[i]= arr[j]
    j = j-1

print(brr)

print("\n 3. using vectorized method")
arr = arr[::-1]
print(arr)

print("\n 4. to create 3x3 matrix with values from 0 to 8")
z = np.arange(9).reshape(3,3)
print(z)

print("\n 5. indices of non-zeros elements")
z= np.array([1,2,0,0,4,0])
i=0
for i in range(6):
    if z[i] != 0:
        print(i)

print("\n 6. using function nonzero to print non-zero elements")
nz= np.nonzero([1,2,0,0,9,0,0])
print(nz)

print("\n 7. 3x3 identity matric")
iarr = np.eye(3)
print(iarr)
