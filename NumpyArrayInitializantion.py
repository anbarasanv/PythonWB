#importing Numpy library
import numpy as np
#making a 2D array using numpy
a = np.array([(1.5,2,3), (4,5,6)])
#complex array
b = np.array([(1.5,2,3), (4,5,6)], dtype = complex)

#In below are the number of ways to create or intialize a array
#the dimention of the array must given in the tupple form
c = np.zeros((3,3))
d = np.ones((2,2))
e = np.empty((2,2))
#In the arrange function start,end,number to be added next stpe
f = np.arange(10,20,1)
'''In the linespace function start,end,number of elements to be extended to be extended. result will be number of elements divide by last number'''
g= np.linspace(1,10,10)
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
