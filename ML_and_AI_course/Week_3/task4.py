import numpy as np

a = np.random.default_rng(42)
b = a.integers(1, 100, size=10)

print(b)
print(b.max(),b.min())