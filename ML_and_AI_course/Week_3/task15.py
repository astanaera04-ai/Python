import numpy as np

A = np.array([[4, 7], [2, 6]])

det_A = np.linalg.det(A)
print(f"Анықтауыш: {det_A:.2f}")

A_inv = np.linalg.inv(A)
print("Кері матрица:\n", A_inv)

I = np.eye(2)
i = np.allclose(A @ A_inv, I)
print("Бірлік матрицаға тең бе:", i)
