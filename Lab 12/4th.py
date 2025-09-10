import numpy as np
import matplotlib.pyplot as plt
t=np.linspace(0,1,1000,endpoint=False)
y1=np.sin(2*np.pi*10*t)
y2=3*y1
plt.plot(t,y1,label="original")
plt.plot(t,y2,label="scaled")
plt.legend()
plt.show()
