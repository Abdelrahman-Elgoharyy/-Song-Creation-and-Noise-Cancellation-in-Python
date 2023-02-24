import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.fftpack import fft

N = 3*1024
𝑓req = np. linspace(0 , 512 , int(𝑁/2))
t = np.linspace(0 , 3 , 12 * 1024)
F = [130.81, 146.83, 164.81, 174.61, 196, 220]
f = [261.63, 293.66, 329.63, 349.23, 392, 440]
T = 0
x = 0

for i in range(0, 6):
    xFirst = np.sin(2 * np.pi * F[i] * t) + np.sin(2 * np.pi * f[i] * t)
    x1 = np.reshape(xFirst * [t >= T], np.shape(t))
    x2 = np.reshape(xFirst * [t >= (T + 0.5)], np.shape(t))
    xFirst = x1 - x2
    x += xFirst
    T += 0.5
x_f = fft(x)
x_f = 2/N * np.abs(x_f [0:np.int(N/2)])
𝑓𝑛1 = np. random. randint(0, 512)
𝑓𝑛2 = np. random. randint(0, 512)
nt = np.sin(2*np.pi*fn1*t) + np.sin(2*np.pi*fn2*t)
xnt = x + nt
xnf = fft(xnt)
xnf = 2/N * np.abs(xnf [0:np.int(N/2)])

highest = (x_f)[0]
for i in range ((x_f).size):
    if ((x_f)[i] > highest):
        highest = (x_f)[i]
highest = np.ceil(highest)
noisefrequency = [0,0]
index = 0
for i in range (xnf.size):
    if (xnf[i] > highest):
        noisefrequency[index] = freq[i]
        index += 1
for i in range (2):
    noisefrequency[i] = np.round(noisefrequency[i])
xfiltered = xnt - (np.sin(2*np.pi * noisefrequency[0] * t) + np.sin(2*np.pi*noisefrequency[1] * t))

xfreqfiltered = fft(xfiltered)
xfreqfiltered  = 2/N * np.abs(xfreqfiltered [0:np.int(N/2)])

plt.subplot(3,2,1)
plt.plot(t,x)
plt.subplot(3,2,2)
plt.plot(freq,x_f)
plt.subplot(3,2,3)
plt.plot(t,xnt)
plt.subplot(3,2,4)
plt.plot(freq,xnf)
plt.subplot(3,2,5)
plt.plot(t,xfiltered)
plt.subplot(3,2,6)
plt.plot(freq,xfreqfiltered)

sd.play (xfiltered , 3*1024)
