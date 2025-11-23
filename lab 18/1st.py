import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

rate1, x = wavfile.read(r"F:\1 SEMESTER\python\1 data\audio1.wav")
rate2, h = wavfile.read(r"F:\1 SEMESTER\python\1 data\audio2.wav")
if x.ndim > 1:
    x = x.mean(axis=1)
if h.ndim > 1:
    h = h.mean(axis=1)
x = x.astype(float)
h = h.astype(float)
linear = np.convolve(x, h)
n = max(len(x), len(h))
circular = np.fft.ifft(np.fft.fft(x, n) * np.fft.fft(h, n)).real
plt.figure(figsize=(12, 6))
plt.subplot(311)
plt.title("Audio 1")
plt.plot(x)
plt.subplot(312)
plt.title("Linear Convolution")
plt.plot(linear)
plt.subplot(313)
plt.title("Circular Convolution")
plt.plot(circular)
plt.tight_layout()
plt.show()
