import numpy as np
a = np.array([[[3, 7, 6], [1, 5, 2]],
              [[1, 2, 4], [7, 2, 9]],
              [[1, 0, 0], [5, 4, 3]],
              [[8, 1, 4], [2, 7, 8]]])
print(a)
print(np.max(a))
print(np.max(a, axis=0))  # Column wise
print()
print(np.max(a, axis=1))  # Row wise
# 6 5
# 4 9
# 1 5
# 8 8
