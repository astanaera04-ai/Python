import numpy as np

m = np.array([[4, 9, 2], [3, 5, 7], [8, 1, 6]])

print(np.sum(m, axis=1), np.sum(m, axis=0))

print(np.round(np.mean(m, axis=1), 2), np.round(np.mean(m, axis=0), 2))

print(np.max(m, axis=1), np.max(m, axis=0))
