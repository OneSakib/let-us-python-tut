import numpy as np
a=np.full(10,3)
print(a)
print(a.nbytes) # one int 8 bit so here is 10 10*8 = 80 bit
print(a.itemsize)  # one int 8 bit

b=np.linspace(0,90,10)
print(b)
b=b[::-1]
print(b)
c=a+b
print(c)