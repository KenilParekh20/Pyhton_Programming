import numpy as np
import matplotlib.pyplot as plt
fs=1000
t=np.linspace(0,1,fs,endpoint=False)
s1=np.sin(2*np.pi*5*t)
s2=np.sin(2*np.pi*10*t)
y=s1+s2
plt.plot(t,y)
plt.show()
