import numpy as np

s = np.array([45, 78, 92, 55, 61, 88, 39, 70])

r = np.where(s >= 60, "өтті", "өтпеді")
print(r)