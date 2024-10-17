import numpy as np
import matplotlib.pyplot as plt

f0 = 50
sp = 1
t0 = 1/f0
N = 1000

ts = t0 / N

t = np.linspace(0, t0, N)
x = sp * np.abs(np.sin(2*np.pi*f0*t))

average = np.average(x)
power = np.average(np.pow(x, 2))

n = np.linspace(0, N, N)

def calculate_ak(k):
    return -2 / N * np.sum(x * np.cos(2*np.pi*k*n/N))

def calculate_bk(k):
    return -2 / N * np.sum(x * np.sin(2*np.pi*k*n/N))

ak = [2*average]
bk = [calculate_bk(0)]
mk = [average]

for k in range(1, 10):
    a = calculate_ak(k)
    b = calculate_bk(k)
    m = (a**2+b**2)**(1/2)
    ak.append(a)
    bk.append(b)
    mk.append(m)


# plot data
plt.plot(t, x)
plt.hlines([power], xmin=0, xmax=t0, colors="r", linestyles="--")
plt.hlines([average], xmin=0, xmax=t0, colors="k", linestyles="--")
plt.show()

# plot fourier
plt.subplot(2, 1, 1)
plt.title("Ak und Bk")
plt.stem(ak, label="Ak")
plt.stem(bk, label="Bk")
plt.legend()

plt.subplot(2, 1, 2)
plt.title("Mk")
plt.stem(mk)
plt.show()