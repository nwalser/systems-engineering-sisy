import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal.windows import hamming, hann

# read signal
fs, s = wavfile.read('aufgabe_1.wav')  # fs sampling frequency, s signal
s = s/32768  # normalize signal

# only take part of signal for fft
t = np.arange(0, len(s))/fs
time_filter = np.where((t >= 0) & (t <= 0.03))
t = t[time_filter]
s = s[time_filter]

# signal properties
Ts = 1 / fs
power = 1 / len(s) * np.sum(np.pow(s, 2))  # median power
rms = np.sqrt(1 / len(s) * np.sum(np.pow(s, 2)))  # rms
peak = np.max(s)

print(f"T0: {0.03}s")
print(f"f0: {1/0.03}Hz")
print(f"Ts: {Ts}s")

# fft
window = np.ones_like(s)  # no window
windowed = s * window

fft_result = np.fft.fft(windowed) / len(windowed)
fft_frequencies = np.fft.fftfreq(len(windowed), 1 / fs)

A_k = 2 * np.real(fft_result)  # cos coefficients
B_k = -2 * np.imag(fft_result)  # sin coefficients

print(f"A_k0: {A_k[0]}s")
print(f"A_k1: {A_k[1]}s")

# approximate signal
f0 = 33.33
s_app = A_k[0] + A_k[1] * np.cos(2*np.pi*t*f0)


# plot all results
fft_filter = np.where((0 <= fft_frequencies) & (fft_frequencies <= 5000))

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
plt.stem(fft_frequencies[fft_filter], np.abs(fft_result[fft_filter]), linefmt='C1-', markerfmt='C1o', basefmt=" ")
plt.xlabel('Frequenz / Hz')
plt.ylabel('abs(X)')
plt.title('Spektrum')
plt.grid()
plt.show()

# plot a_k, b_k
plt.stem(fft_frequencies[fft_filter], A_k[fft_filter], linefmt='C0-', markerfmt='C0o', basefmt=" ", label='A_k (Cos)')
plt.stem(fft_frequencies[fft_filter], B_k[fft_filter], linefmt='C1-', markerfmt='C1o', basefmt=" ", label='B_k (Sin)')
plt.xlabel('Frequenz / Hz')
plt.ylabel('Amplitude')
plt.title('Fourier-Koeffizienten')
plt.grid()
plt.show()

# plot approximated signal
plt.plot(t, s, t, s_app)
plt.grid(True)
plt.xlabel('t / s')
plt.ylabel('s(t)')
plt.title('Approximated Signal')
plt.show()
