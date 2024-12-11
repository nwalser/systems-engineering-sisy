import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

fs, s = wavfile.read('aufgabe_2.wav')
print("fs = " + str(fs))
s = s/32768

s = s[0:250]

N = len(s)

# plot Zeitsignal
t = np.arange(0, N)/fs

# FFT anwenden
fft_result = np.fft.fft(s) / N  # Normierung auf die Anzahl der Punkte
frequencies = np.fft.fftfreq(N, t[-1] / N)  # Frequenzen bestimmen

# Nur die positiven Frequenzen betrachten
# positive_freq_indices = np.where(frequencies >= 0)
# frequencies = frequencies[positive_freq_indices]
# fft_result = fft_result[positive_freq_indices]

# A_k und B_k berechnen
A_k = 2 * np.real(fft_result)  # Kosinus-Koeffizienten
B_k = -2 * np.imag(fft_result) # Sinus-Koeffizienten

# Ergebnisse anzeigen
plt.stem(frequencies, A_k, linefmt='C0-', markerfmt='C0o', basefmt=" ", label='A_k (Kosinus)')
plt.stem(frequencies, B_k, linefmt='C1-', markerfmt='C1o', basefmt=" ", label='B_k (Sinus)')
plt.xlabel('Frequenz (Hz)')
plt.ylabel('Koeffizienten')
plt.legend()
plt.title('Fourier-Koeffizienten')
plt.grid()
plt.show()

plt.figure(1)
plt.subplot(2, 1, 1)
plt.plot(1000*t, s)

plt.grid(True)
plt.xlabel('t / ms')
plt.ylabel('s(t)')
plt.show()
