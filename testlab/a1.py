import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

fs, x = wavfile.read('aufgabe_1.wav')
print("fs = " + str(fs))
x = x/32768
N = len(x)

# plot Zeitsignal
t = np.arange(0, N)/fs

print(f"Ts: {t[1]-t[0]}s")
print(f"Peak {np.max(x)}")

power = 1 / N * np.sum(np.pow(x, 2))
print(f"Power {power}")

rms = np.sqrt(1 / N * np.sum(np.pow(x, 2)))
print(f"RMS: {rms}")

plt.figure(1)
plt.subplot(2,1,1)
plt.plot(1000*t, x)

plt.grid(True)
plt.xlabel('t / ms')
plt.ylabel('x[n]')
plt.show()
