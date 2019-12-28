import numpy as np
import matplotlib.pyplot as plt

t1 = np.arange(5,9)
print('this is t1',t1)
print(t1.shape)

point = np.arange(-5,0,1)
print('point array looks like',point,'next is \n')
xs, ys = np.meshgrid(point,point)
print(xs,'\n next is \n ',ys)

z = np.sqrt(xs**2 + ys**2)
print(z.astype(int))
plt.imshow(z,cmap=plt.cm.gray);plt.colorbar()
plt.title("image of the plot")
plt.show()
