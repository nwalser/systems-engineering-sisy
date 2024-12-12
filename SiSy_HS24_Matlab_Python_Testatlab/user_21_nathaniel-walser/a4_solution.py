import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal.windows import hamming, hann

# read signal
fs, s = wavfile.read('aufgabe_4.wav')  # fs sampling frequency, s signal
s = s/32768  # normalize signal

# only take part of signal for fft
t = np.arange(0, len(s))/fs
time_filter = np.where((t >= 0) & (t <= 0.08))
t = t[time_filter]
s = s[time_filter]

# signal properties
Ts = 1 / fs

# fft
window = np.ones_like(s)  # no window
windowed = s * window

fft_result = np.fft.fft(windowed) / len(windowed)
fft_frequencies = np.fft.fftfreq(len(windowed), 1 / fs)

max_index = np.argmax(np.abs(fft_result))
print(f"Max Frequency: {np.abs(fft_frequencies)[max_index]}")
c = 3 * 10**8
f0 = 24 * 10**9
print(f"Velocity: {np.abs(fft_frequencies)[max_index] * c / f0}m/s")
print(f"Velocity: {np.abs(fft_frequencies)[max_index] * c / f0 * 3.6}km/h")
print(f"Velocity min: {np.abs(fft_frequencies)[1] * c / f0}m/s")
print(f"Velocity max: {4000 * c / f0}m/s")
print(fft_frequencies[-1])

# plot all results
fft_filter = np.where((0 <= fft_frequencies) & (fft_frequencies <= 10000))

# plot signal
plt.plot(t, s)
plt.grid(True)
plt.xlabel('t / s')
plt.ylabel('s(t)')
plt.title('Signal')
plt.show()

# plot spectrum
plt.stem(fft_frequencies[fft_filter], np.abs(fft_result[fft_filter]), linefmt='C1-', markerfmt='C1o', basefmt=" ")
plt.xlabel('Frequenz / Hz')
plt.ylabel('abs(X)')
plt.title('Spektrum')
plt.grid()
plt.show()