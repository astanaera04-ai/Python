import numpy as np

values = np.array([3, -2, 7, -5, 0, 8, -1])
values[values < 0] = 0

print(values)