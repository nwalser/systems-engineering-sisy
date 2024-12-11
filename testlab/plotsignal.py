# Signale plotten

""" doc string """

import numpy as np
import matplotlib.pyplot as plt
# Alternative: import pylab as pl

# graphical backend in spyder: preferences - IPython console - Graphics - Graphics backend - Qt5
# Alternative: %matplotlib qt

plt.close()  # closes old windows / figures

# Parameter
N = 200         # Number of Samples
f0 = 1000       # Frequenz
fs = 100000     # Abtastfrequenz

# Vektoren initialisieren
t = np.zeros(N)
x = np.zeros(N)
y = np.zeros(N)
z = np.zeros(N)

# Signale generieren
for n in range(N): # n geht von 0...N-1
    t[n] = n/fs
    x[n] = np.sin(2*np.pi*f0*t[n])
    y[n] = np.sin(2*np.pi*3*f0*t[n])/3
    z[n] = x[n] + y[n]
      
# Alternative: t = np.linspace(0, N, N, endpoint=False)/fs
# Alternative Vektor-basiert aehnlich wie in Matlab
# t = np.arange(0,N)/fs
# x = np.sin(2*np.pi*f0*t)

# Plots
plt.figure(1)
plt.subplot(2,1,1)
plt.plot(1000*t,x,'-',1000*t,y,'--')
# Alternative: 2 mal nacheinander plot mit nur 1 Signal
plt.grid(True)
plt.xlabel('t / ms')
plt.ylabel('Amplitude / V')
plt.title('Signale')

plt.xlim([0, 2.5])
plt.ylim([-1.5, 1.5])
plt.legend(['x(t)','y(t)'])


plt.subplot(2,1,2)
plt.plot(1000*t,z)

plt.grid(True)
plt.xlabel('t / ms')
plt.ylabel('z(t)')

plt.xlim([0, 2.5])
plt.ylim([-1.5, 1.5])

plt.tight_layout()

plt.show()