import numpy as np
import matplotlib.pyplot as plt
import scipy.signal
from scipy.io import wavfile
from scipy.fft import fft
from scipy.signal import find_peaks

plt.close()

fs, x = wavfile.read('dtmf_signal.wav')
print("fs = " + str(fs))
x = x/32768
N = len(x)

# plot time signal
plt.figure(1)
plt.subplot(2, 1, 1)

t = np.arange(0, N) * 1/fs
plt.plot(t, x)
plt.grid(True)
plt.xlabel('t / ms')
plt.ylabel('x[n]')

lut = np.array(
    (1336, )
)

# Ziffer detektieren
for i in np.arange(1, 20, 2):
    N = 400
    f = np.arange(0, N)*fs/N
    X = fft(x[i*N:(i+1)*N])/N
    plt.subplot(2, 1, 2)
    plt.plot(f, abs(X))

    plt.grid(True)
    plt.xlabel('f / Hz')
    plt.ylabel('abs(X[m])/N')

    peaks, _ = find_peaks(abs(X), height=0.1)
    plt.plot(abs(f[peaks]), abs(X[peaks]), "x")
    print(f"F1: {abs(f[peaks])} - F2 {abs(f[peaks])}")

plt.tight_layout()
plt.show()