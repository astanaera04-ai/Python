import numpy as np

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
v = np.vstack((x, y))
h = np.hstack((x, y))

print(v)
print(h)