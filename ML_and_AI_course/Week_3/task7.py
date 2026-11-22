import numpy as np

scores = np.array([45, 78, 92, 55, 61, 88, 39, 70])
b = scores[scores > 60]
print(b)
print(b.size)