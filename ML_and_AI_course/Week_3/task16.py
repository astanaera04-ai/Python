import numpy as np

A = np.array([[3, 2], [1, -1]])
B = np.array([12, 1])

s = np.linalg.solve(A, B)
print(s)