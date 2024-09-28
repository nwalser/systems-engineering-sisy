import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

f = 400

velocity = np.loadtxt('3a_data.csv', delimiter=',')
acceleration = np.gradient(velocity)
angle = sp.integrate.cumulative_trapezoid(velocity, dx=1/f, initial=0)

t = np.linspace(0, len(velocity) / f, len(velocity))

angle_max_index = np.argmax(angle)
angle_min_index = np.argmin(angle)

print(f"Max Time: {angle_max_index/f}")
print(f"Max Position: {angle[angle_max_index]}")
print(f"Max Position Velocity: {velocity[angle_max_index]}")
print(f"Max Position Acceleration: {acceleration[angle_max_index]}")

print(f"Min Time: {angle_min_index/f}")
print(f"Min Position: {angle[angle_min_index]}")
print(f"Min Position Velocity: {velocity[angle_min_index]}")
print(f"Min Position Acceleration: {acceleration[angle_min_index]}")


# plot
plt.figure(1, figsize=(12, 8))

# angle acceleration
plt.subplot(3, 1, 1)
plt.plot(t, acceleration)
plt.grid(True)
plt.ylabel('Acceleration [°/s^2]')

# angle velocity
plt.subplot(3, 1, 2)
plt.plot(t, velocity)
plt.grid(True)
plt.ylabel('Velocity [°/s]')

# angle position
plt.subplot(3, 1, 3)
plt.plot(t, angle)
plt.grid(True)
plt.xlabel('Time [s]')
plt.ylabel('Angle [°]')

plt.show()
