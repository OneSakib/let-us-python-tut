import numpy as np
a = np.ones((5, 5))  # 5x5 =25 items
'''
[[1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]]
'''
print(a)
a[1:1, 1:-1] = 3  # index 1 row to 1 row and 1 column to -1 colun means end
''''
Result will be like
[[1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]]

Same result beacuse row selected 1 to 1 means not any row
'''
print()
print(a, end="\n\n")


b = np.ones((4, 3))
c = np.full((3, 5), 2)
print(b, end="\n\n")
print(c, end="\n\n")
d = b@c
print(d, end="\n\n")
e = np.arange(11)
print(e, end="\n\n")
e[(2 < e) & (e < 8)] *= -1
print(e)
