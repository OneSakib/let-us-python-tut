import numpy as np
a = np.arange(20).reshape((5, 4))
print(a)
print(np.sum(a))
print(np.sum(a, axis=0))  # Column wise
print()
print(np.sum(a, axis=1))  # row wise
