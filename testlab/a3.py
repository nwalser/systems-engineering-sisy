import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

fs, s = wavfile.read('aufgabe_3.wav')
print("fs = " + str(fs))
Ts = 1/fs
print("Ts = " + str(Ts))

s = s[0:4000]
s = s/32768
N = len(s)

# plot Zeitsignal
t = np.arange(0, N)/fs


fft_result = np.fft.fft(s) / N
fft_frequencies = np.fft.fftfreq(N, Ts)


A_k = 2 * np.real(fft_result)  # Kosinus-Koeffizienten
B_k = -2 * np.imag(fft_result) # Sinus-Koeffizienten

sapp = np.zeros(N)

for i in range(0, 6):
    sapp += A_k[i] * np.cos(2*np.pi*t*fft_frequencies[i])
    sapp += B_k[i] * np.sin(2*np.pi*t*fft_frequencies[i])


plt.figure(1)
plt.subplot(2,1,1)
plt.plot(1000*t,s,'-',1000*t,sapp,'--')

plt.grid(True)
plt.xlabel('t / ms')
plt.legend(['s(t)', 'sapp(t)'])
plt.show()