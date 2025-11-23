import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

_, clean = wavfile.read(r"F:/1 SEMESTER/python/1 data/audio2.wav")
_, noisy = wavfile.read(r"F:/1 SEMESTER/python/1 data/audio1.wav")
_, periodic = wavfile.read(r"F:/1 SEMESTER/python/1 data/audio2.wav")

if clean.ndim > 1:
    clean = clean.mean(axis=1)
if noisy.ndim > 1:
    noisy = noisy.mean(axis=1)
if periodic.ndim > 1:
    periodic = periodic.mean(axis=1)

clean = clean.astype(float)
noisy = noisy.astype(float)
periodic = periodic.astype(float)

cross = np.correlate(clean, noisy, mode="full")
auto_clean = np.correlate(clean, clean, mode="full")
auto_noisy = np.correlate(noisy, noisy, mode="full")
auto_periodic = np.correlate(periodic, periodic, mode="full")

plt.figure(figsize=(12, 8))

plt.subplot(221)
plt.title("Cross-Correlation Clean vs Noisy")
plt.plot(cross)

plt.subplot(222)
plt.title("Autocorrelation Clean")
plt.plot(auto_clean)

plt.subplot(223)
plt.title("Autocorrelation Noisy")
plt.plot(auto_noisy)

plt.subplot(224)
plt.title("Autocorrelation Periodic")
plt.plot(auto_periodic)

plt.tight_layout()
plt.show(block=True)
