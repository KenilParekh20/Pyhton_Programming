import numpy as np
import matplotlib.pyplot as plt
fs=500
t=np.linspace(0,2,fs*2,endpoint=False)
s1=np.sin(2*np.pi*5*t)
s2=np.cos(2*np.pi*10*t)
y=s1*s2
plt.plot(t,y)
plt.show()
