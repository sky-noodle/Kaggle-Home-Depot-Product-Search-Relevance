import numpy as np 
import time
import math
# from enthought.mayavi import mlab
import matplotlib.pyplot as plt

# a = np.array([1,2,3,4])
# b= np.array([[1,2,3],[2,3,4],[2]])


# def  func2(i,j):
# 	return (i+1)*(j+1)

# c=np.fromfunction(func2,(9,9))

# # print(c)
# np.arange(0,60,10).reshape(-1,1)+np.arange(0,6

# persontype = np.dtype({
# 	'names':['name', 'age', 'weight'],
# 	'formats':['S32', 'i', 'f']
# 	})
# a=np.array([("Zhang",32,75.5),("Wang",24,65.2)], dtype=persontype)
# print a.dtype

# x = [i*0.001 for i in xrange(1000000)]
# start = time.clock()
# for i,t in enumerate(x):
# 	x[i] = math.sin(t)

# print "math.sin:", time.clock()-start

# y = [i*0.001 for i in xrange(1000000)]
# y = np.array(y)
# starts = time.clock()
# np.sin(y,y)
# print "numpy.sin:", time.clock()-starts

# x,y = np.ogrid[-2:2:20j,-2:2:20j]
# z = x*np.exp(-x**2 - y**2)

# pl = mlab.surf(x,y,z,warp_scale="auto")
# mlab.axes(xlabel='x', ylabel='y', zlabel='z')
# mlab.outline(pl)

plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()


