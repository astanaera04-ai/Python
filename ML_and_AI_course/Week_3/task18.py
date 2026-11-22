import numpy as np

a = np.array([0, 30, 45, 60, 90])
radians = np.radians(a)

sin_v = np.round(np.sin(radians), 3)
cos_v = np.round(np.cos(radians), 3)

print(sin_v)
print(cos_v)