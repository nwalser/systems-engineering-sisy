import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal.windows import hamming, hann

# read signal
fs, s = wavfile.read('aufgabe_5.wav')  # fs sampling frequency, s signal
s = s/32768  # normalize signal

# only take part of signal for fft
t = np.arange(0, len(s))/fs
time_filter = np.where((t >= 0) & (t <= 10))
t = t[time_filter]
s = s[time_filter]

# signal properties
Ts = 1 / fs

# fft
window = hamming(len(s))
windowed = s * window

fft_result = np.fft.fft(windowed) / len(windowed)
fft_frequencies = np.fft.fftfreq(len(windowed), 1 / fs)

print(f"Frequency Resolution: {fft_frequencies[1]-fft_frequencies[0]}Hz")

# plot all results
fft_filter = np.where((0 <= fft_frequencies) & (fft_frequencies <= 10000))

# plot signal
plt.plot(t, s)
plt.grid(True)
plt.xlabel('t / s')
plt.ylabel('s(t)')
plt.title('Signal')
plt.show()

# plot signal windowed
plt.subplot(2, 1, 1)
plt.title('Signal Windowed')
plt.plot(t, window)
plt.grid(True)
plt.xlabel('t / s')
plt.ylabel('Scalar')
plt.subplot(2, 1, 2)
plt.plot(t, windowed)
plt.grid(True)
plt.xlabel('t / s')
plt.ylabel('s(t)')
plt.show()

# plot spectrum
plt.plot(fft_frequencies[fft_filter], 20 * np.log10(np.abs(fft_result[fft_filter])), marker='o')
plt.xlabel('Frequenz / Hz')
plt.ylabel('abs(X) / dB')
plt.title('Spektrum')
plt.grid()
plt.show()