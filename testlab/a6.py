# Aufgabe 6

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.fft import fft
from scipy.signal.windows import hamming, hann

plt.close()  # closes old windows / figures

fs, x = wavfile.read('aufgabe_6.wav')
print("fs = " + str(fs))
x = x/32768 # Spaltenvektor, Elemente sind float-Werte [-1,1]
N = len(x)  # Laenge von x

t = np.arange(0, N) / fs

print(f"Signaldauer: {N/fs}s")

fft_result = np.fft.fft(x) / N
fft_frequencies = np.fft.fftfreq(N, 1/fs)

max_freq_index = np.argmax(fft_result[np.where(fft_frequencies >= 0)])
print(f"Max Frequency: {fft_frequencies[max_freq_index]}Hz")

print(f"Genauigkeitsinterval: {(fft_frequencies[1]-fft_frequencies[0])/2}Hz")

plt.plot(t, x)
plt.show()

plt.stem(fft_frequencies[0:1000], np.abs(fft_result)[0:1000],
         linefmt='C1-', markerfmt='C1o', basefmt=" ")
plt.xlabel('Frequenz (Hz)')
plt.ylabel('Koeffizienten')
plt.title('Fourier-Koeffizienten')
plt.grid()
plt.show()