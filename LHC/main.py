import numpy as np
import matplotlib.pyplot as plt

# Import
from signal_ICT_Kenil_parekh_92400133150.unitary_signals import unit_step,unit_impulse,ramp_signal
from signal_ICT_Kenil_parekh_92400133150.trigonometric_signals import sine_wave,cosine_wave
from signal_ICT_Kenil_parekh_92400133150.operations import time_shift,signal_addition,signal_multiplication

n=np.arange(0,20)  #Length 20
#Continuous time for sine/cosine signals
t=np.linspace(0,1,500)  #0 to 1 sec, 500 samples

#Generate discrete signals
u=unit_step(n)
d=unit_impulse(n)
r=ramp_signal(n)

#Generate sine and cosine waves
sine=sine_wave(2,5,0,t)   
cosine=cosine_wave(1,5,0,t)  
#Time shift sine wave by +5 units
shifted_t, shifted_sine=time_shift(sine,np.arange(len(sine)),5)

#Addition of unit step and ramp
sum_signal=signal_addition(u,r,n)

#Multiply sine and cosine waves
product=signal_multiplication(sine,cosine,np.arange(len(sine)))

plt.figure(figsize=(15,10))

plt.subplot(3,2,1)
plt.stem(n,u)
plt.title("Unit Step (length 20)")

plt.subplot(3,2,2)
plt.stem(n,d)
plt.title("Unit Impulse (length 20)")

plt.subplot(3,2,3)
plt.plot(t,sine)
plt.title("Sine Wave (Amplitude=2, Freq=5Hz)")

plt.subplot(3,2,4)
plt.plot(np.arange(len(sine)),sine,label="Original")
plt.plot(shifted_t,shifted_sine,label="Shifted +5")
plt.title("Time Shift of Sine Wave")
plt.legend()

plt.subplot(3,2,5)
plt.stem(n,sum_signal)
plt.title("Unit Step+Ramp")

plt.subplot(3,2,6)
plt.plot(t,product)
plt.title("Sine*Cosine")

plt.tight_layout()
plt.show()
