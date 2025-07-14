import numpy as np
a = np.array([11, 22, 0, 0, 40, 50, 0])
print(np.nonzero(a), end="\n\n")
b = np.eye(5)
print(b, end="\n\n")
c = np.random.random((4, 4))
print(c, end="\n\n")
mn = c.min()
print(mn, end="\n\n")
mx = c.max()
print(mx, end="\n\n")
d = np.zeros((8, 8), int)
print(d, end="\n\n")

'''
[[0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0]]
 '''

d[1::2, ::2] = 1

'''
Expected results
  -   -   -   -   
[[0 0 0 0 0 0 0 0]
 [1 0 1 0 1 0 1 0] --
 [0 0 0 0 0 0 0 0]
 [1 0 1 0 1 0 1 0] --
 [0 0 0 0 0 0 0 0]
 [1 0 1 0 1 0 1 0] --
 [0 0 0 0 0 0 0 0]
 [1 0 1 0 1 0 1 0]] --

'''
print(d, end="\n\n")

d[::2, 1::2] = 1
'''
Expected Result

    -   -   -   -   
[[0 1 0 1 0 1 0 1] --
 [1 0 1 0 1 0 1 0] 
 [0 1 0 1 0 1 0 1] --
 [1 0 1 0 1 0 1 0] 
 [0 1 0 1 0 1 0 1] --
 [1 0 1 0 1 0 1 0] 
 [0 1 0 1 0 1 0 1] --
 [1 0 1 0 1 0 1 0]] 


'''
print(d,end="\n\n")
