# Aufgabe 5

import numpy as np
import matplotlib.pyplot as plt

from scipy.fft import fft
from scipy.signal.windows import hamming, hann

plt.close()  # closes old windows / figures

# Parameter
fs = 1e4
f0 = 1000 
N = 16

# plot Zeitsignal
t = np.arange(0, N) / fs
x = np.sin(2*np.pi*f0*t)


fft_result = np.fft.fft(x) / N
fft_frequencies = np.fft.fftfreq(N, 1/fs)


plt.figure(1)
plt.subplot(2, 1, 2)
plt.stem(fft_frequencies, np.abs(fft_result),
         linefmt='C1-', markerfmt='C1o', basefmt=" ")
plt.xlabel('Frequenz (Hz)')
plt.ylabel('abs')
plt.legend()
plt.title('Spektrum')
plt.grid()


plt.subplot(2, 1, 1)
plt.plot(t, x,'o')

plt.grid(True)
plt.xlabel('t / ms')
plt.ylabel('x[n]')


plt.tight_layout()

plt.show()
