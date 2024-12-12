import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal.windows import hamming, hann

fs = 100
N = 100
t = np.arange(0, N)/fs

A_k = [0, 0, 5, 2]
B_k = [0, 0, -5, 2]

fft_frequencies = np.fft.fftfreq(N, 1 / fs)

# approximate signal
s_app1 = np.zeros_like(t)
for i in range(0, len(A_k)):  # approximate to 2 coefficients
    s_app1 += A_k[i] * np.cos(2*np.pi*t*fft_frequencies[i])

# approximate signal
s_app2 = np.zeros_like(t)
for i in range(0, len(A_k)):  # approximate to 2 coefficients
    s_app2 += B_k[i] * np.sin(2*np.pi*t*fft_frequencies[i])



plt.plot(t, s_app1)
plt.grid(True)
plt.xlabel('t / s')
plt.ylabel('s1(t)')
plt.title('Approximated Signal')
plt.show()

plt.plot(t, s_app2)
plt.grid(True)
plt.xlabel('t / s')
plt.ylabel('s2(t)')
plt.title('Approximated Signal')
plt.show()

# plot approximated signal
plt.plot(s_app1, s_app2)
plt.grid(True)
plt.xlabel('s2(t)')
plt.ylabel('s1(t)')
plt.title('Approximated Signal')
plt.show()