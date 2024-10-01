import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

f_decimal = '{0:.2f}'
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
plt.figure(1)

# angle acceleration
plt.subplot(3, 1, 1)
plt.title("IMU Tire Signal")
plt.plot(t, acceleration)
plt.grid(True)
ax = plt.gca()
ax.set_xticklabels([])
plt.ylabel('Acceleration [°/s^2]')
plt.vlines([angle_max_index/f, angle_min_index/f], ymin=-4, ymax=4, color="k", linestyle='--')
plt.text(x=4.3, y=0.5, s=f"Accel. \n"
                       f"{f_decimal.format(acceleration[angle_min_index])}°/s^2 \n"
                       f"{f_decimal.format(acceleration[angle_max_index])}°/s^2")


# angle velocity
plt.subplot(3, 1, 2)
plt.plot(t, velocity)
plt.grid(True)
ax = plt.gca()
ax.set_xticklabels([])
plt.ylabel('Velocity [°/s]')
plt.vlines([angle_max_index/f, angle_min_index/f], ymin=-210, ymax=210, color="k", linestyle='--')
plt.text(x=4.3, y=40, s=f"Vel: \n"
                       f"{f_decimal.format(velocity[angle_min_index])}°/s \n"
                       f"{f_decimal.format(velocity[angle_max_index])}°/s")

# angle position
plt.subplot(3, 1, 3)
plt.plot(t, angle)
plt.grid(True)
ax = plt.gca()
plt.ylabel('Angle [°]')
plt.xlabel('Time [s]')
plt.vlines([angle_max_index/f, angle_min_index/f], ymin=-5, ymax=210, color="k", linestyle='--')
plt.text(x=4.3, y=120, s=f"Angle: \n"
                         f"{f_decimal.format(angle[angle_min_index])}° \n"
                         f"{f_decimal.format(angle[angle_max_index])}°")

plt.text(x=0.2, y=120, s=f"\n"
                       f"t Max: {f_decimal.format(angle_max_index/f)}s \n"
                       f"t Min: {f_decimal.format(angle_min_index/f)}s")

plt.show()
