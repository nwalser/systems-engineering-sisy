import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

fs, x = wavfile.read('aufgabe_4.wav')
print("fs = " + str(fs))
x = x/32768
N = len(x)

# plot Zeitsignal
t = np.arange(0, N)/fs

mask = np.zeros_like(t)
y = np.zeros_like(t)

Ts = 1 / fs
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