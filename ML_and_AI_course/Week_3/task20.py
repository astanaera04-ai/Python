import numpy as np

salaries = np.array([250, 280, 300, 310, 320, 350, 2000])

mean_val = np.mean(salaries)
median_val = np.median(salaries)
std_val = np.std(salaries)

print(f"{mean_val:.1f}")
print(f"{median_val:.1f}")
print(f"{std_val:.1f}")