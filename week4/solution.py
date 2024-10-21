import numpy as np
import matplotlib.pyplot as plt

elements = 10

f0 = 50
sp = 1
t0 = 1/f0
N = 1000

ts = t0 / N

t = np.linspace(0, t0, N)
# x = sp * np.abs(np.sin(2*np.pi*f0*t))  # positive sinus
# x = sp * np.sin(2*np.pi*f0*t)  # normal sinus
# x = t  # linear
# cos = np.cos(2*np.pi*f0*t)
# x = sp * np.where(cos < 0, 0, cos)  # positive sinus
x = np.floor(np.sin(2*np.pi*f0*t)) + 0.5

# calculate features
average = np.average(x)
power = np.average(np.pow(x, 2))

# calculate fft
ks = np.arange(start=0, stop=elements, step=1)
ak = np.zeros_like(ks, dtype=np.float64)
bk = np.zeros_like(ks, dtype=np.float64)
mk = np.zeros_like(ks, dtype=np.float64)
phik = np.zeros_like(ks, dtype=np.float64)

ak[0] = 2*average
bk[0] = 0
mk[0] = ak[0]/2

n = np.linspace(0, N, N)

for k in ks:
    ak[k] = 2 / N * np.sum(x * np.cos(2*np.pi*k*n/N))
    bk[k] = 2 / N * np.sum(x * np.sin(2*np.pi*k*n/N))

mk[1:] = (ak[1:] ** 2 + bk[1:] ** 2) ** (1 / 2)
phik = -np.arctan2(bk, ak)

power_parseval = mk[0]**2 + np.sum(np.pow(mk[1:], 2)) / 2


def fourier_signal(t):
    signal = np.zeros_like(t)

    for i in range(0, len(t)):
        signal[i] = (ak[0] / 2
                     + np.sum(ak[1:] * np.cos(2 * np.pi * ks[1:] * f0 * t[i]))
                     + np.sum(bk[1:] * np.sin(2 * np.pi * ks[1:] * f0 * t[i])))

    return signal


# plot function
plt.plot(t, x)
plt.plot(t, fourier_signal(t))

plt.hlines([power], xmin=0, xmax=t0, colors="r", linestyles="--")
plt.hlines([power_parseval], xmin=0, xmax=t0, colors="b", linestyles="--")
plt.hlines([average], xmin=0, xmax=t0, colors="k", linestyles="--")
plt.show()

# plot fourier ak bk
plt.subplot(2, 1, 1)
plt.title("Ak")
plt.stem(np.round(ak, 2), label="Ak")
plt.legend()

plt.subplot(2, 1, 2)
plt.title("Bk")
plt.stem(np.round(bk, 2), label="Bk")
plt.legend()
plt.show()

# plot mk phik
plt.subplot(2, 1, 1)
plt.title("Mk")
plt.stem(np.round(mk, 2), label="Mk")
plt.legend()

plt.subplot(2, 1, 2)
plt.title("Phik")
plt.stem(np.round(phik, 2), label="Phik")
plt.legend()
plt.show()

