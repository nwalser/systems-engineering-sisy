import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

Ts = 0.000001
f0 = 1000
t = np.arange(0, 3*1/f0, Ts)
x = np.cos(2*np.pi*1000*t)

N = len(x)

# plot Zeitsignal
mask = np.zeros_like(t)
y = np.zeros_like(t)

tau = 0.0016

h = Ts / tau * np.exp(-t / tau)
y = np.convolve(h, x)


plt.figure(1)
plt.subplot(2, 1, 1)
plt.plot(1000*t, x)
plt.plot(1000*t, y[0:N])
plt.plot(1000*t, mask)

plt.grid(True)
plt.xlabel('t / ms')
plt.legend(['x(t)', 'y(t)'])

plt.show()