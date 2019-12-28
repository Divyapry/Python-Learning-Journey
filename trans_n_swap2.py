import numpy as np

print("1. one D array")

a1 = np.array([[1,2,3,4]])
"""to print transpose using T attribute"""
print(np.transpose(a1))
"""to swap axes in 1D array"""
print(np.swapaxes(a1,0,1))
print(np.swapaxes(a1,1,0))# either way it swaps the 2 dimensions of 1 d arrays






print("\n 2. two D array")
a2 = np.arange(12).reshape(2,2,3)
print(a2)

print(" TRANSPOSE OF 2D MATRIX IS: \n")
"""SYNTAX:TRANSPOSE(INPUT ARRAY,AXES=NONE OR SPECIFY)"""

print(np.transpose(a2))
print(np.transpose(a2,(1,2,0)))


"""GIVEN ARRAY IS (2,2,3) AND ITS TRANSPOSE IS (3,2,2) THAT
IS 3D array WITH 2 ROWS AND 2 COLUMNS"""

print(" swap axes for 2d array: \n")

"""SYNTAX:SWAPAXES(INPUT ARRAY, AXIS 1, AXIS 2)"""
"""IN A2, AXIS 0=2; AXIS 1 =2; AXIS 2 =3"""

print(np.swapaxes(a2,2,1))
