import numpy as np

accelerations = np.array([2.8823, -0.0242, 9.3673])
gravitation = np.sqrt(np.sum(accelerations**2))

print(f"Gravitation: {gravitation} m/s^2")

# alpha = arctan(x / z)
alpha = np.arctan(accelerations[0] / accelerations[2])

print(f"Alpha: {alpha} rad")
print(f"Alpha: {alpha * 180 / np.pi} °")
