import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal.windows import hamming, hann

fs = 100000
f0 = 1000
t = np.arange(0, 1000)/fs
s = 0.5*np.sin(2 * np.pi * f0 * t)

# only take part of signal for fft
time_filter = np.where((t >= 0) & (t <= 10))
t = t[time_filter]
s = s[time_filter]

# signal properties
Ts = 1 / fs
power = 1 / len(s) * np.sum(np.pow(s, 2))  # median power
rms = np.sqrt(1 / len(s) * np.sum(np.pow(s, 2)))  # rms
peak = np.max(s)

# fft
window = np.ones_like(s)  # no window
# window = hann(len(s))
# window = hamming(len(s)),
windowed = s * window

fft_result = np.fft.fft(windowed) / len(windowed)
fft_frequencies = np.fft.fftfreq(len(windowed), 1 / fs)

A_k = 2 * np.real(fft_result)  # cos coefficients
B_k = -2 * np.imag(fft_result)  # sin coefficients

# approximate signal
s_app = np.zeros_like(s)
for i in range(0, 3):  # approximate to 2 coefficients
    s_app += A_k[i] * np.cos(2*np.pi*t*fft_frequencies[i])
    s_app += B_k[i] * np.sin(2*np.pi*t*fft_frequencies[i])

# inpulse response
tau = 0.0016
h = np.ones(2); h[1] = -1  # example response
s_out = np.convolve(h, s)[0:len(s)]

# plot all results
fft_filter = np.where((0 <= fft_frequencies) & (fft_frequencies <= 5000))

# plot signal
plt.plot(t, s, label="Signal")
plt.plot(t, s_out, label="Signal out")
plt.grid(True)
plt.xlabel('t / s')
plt.ylabel('s(t)')
plt.title('Signal')
plt.legend()
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

# plot signal out
plt.plot(t, s_out)
plt.grid(True)
plt.xlabel('t / s')
plt.ylabel('s(t)')
plt.title('Signal Out')
plt.show()

# plot spectrum
plt.stem(fft_frequencies[fft_filter], np.abs(fft_result[fft_filter]), linefmt='C1-', markerfmt='C1o', basefmt=" ")
plt.xlabel('Frequenz / Hz')
plt.ylabel('abs(X)')
plt.title('Spektrum')
plt.grid()
plt.show()

# plot spectrum
plt.plot(fft_frequencies[fft_filter], 20 * np.log10(np.abs(fft_result[fft_filter])), marker='o')
plt.xlabel('Frequenz / Hz')
plt.ylabel('abs(X) / dB')
plt.title('Spektrum')
plt.grid()
plt.show()

# plot angle
plt.stem(fft_frequencies[fft_filter], np.angle(fft_result[fft_filter]), linefmt='C1-', markerfmt='C1o', basefmt=" ")
plt.xlabel('Frequenz / Hz')
plt.ylabel('angle(X) / rad')
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
plt.plot(t, s_app)
plt.grid(True)
plt.xlabel('t / s')
plt.ylabel('s(t)')
plt.title('Approximated Signal')
plt.show()