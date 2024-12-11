# Aufgabe 7

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.fft import fft
from scipy.signal.windows import hamming, hann

plt.close()  # closes old windows / figures

fs, x = wavfile.read('aufgabe_7.wav')
print("fs = " + str(fs))
x = x/32768 # Spaltenvektor, Elemente sind float-Werte [-1,1]
N = len(x)  # Laenge von x

# plot Zeitsignal
t = np.arange(0, N)/fs

fft_result = np.fft.fft(x*hann(N)) / N
fft_frequencies = np.fft.fftfreq(N, 1/fs)

plt.figure(1)
plt.subplot(2, 1, 2)
plt.plot(fft_frequencies[0:100],
         20 * np.log10(np.abs(fft_result[0:100])), color='b', marker='o')
plt.xlabel('Frequenz (Hz)')
plt.ylabel('Koeffizienten')
plt.title('Fourier-Koeffizienten')
plt.grid()


plt.subplot(2, 1, 1)
plt.plot(1000*t, x)

plt.grid(True)
plt.xlabel('t / ms')
plt.ylabel('x[n]')

plt.tight_layout()

plt.show()
