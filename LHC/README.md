# signal_ICT_Kenil_parekh_92400133150

This is my Python package for the ICT course.  
The package contains functions for basic signal generation and signal operations.  

- unitary_signals - unit_step, unit_impulse, ramp  
- trigonometric_signals - sine_wave, cosine_wave, exponential  
- operations - time_shift, time_scaling, signal_addition, signal_multiplication  

# Files in the Package
- unitary_signals.py - unit_step, unit_impulse, ramp  
- trigonometric_signals.py - sine_wave, cosine_wave, exponential  
- operations.py - time_shift, time_scaling, signal_addition, signal_multiplication  
- main.py - runs examples and shows plots  

# Installation
## Local Install (from wheel file)
First, build the package:
python setup.py sdist bdist_wheel

Then install it locally:
pip install dist/signal_ICT_Kenil_parekh_92400133150-0.1-py3-none-any.whl

## Upload & Install from TestPyPI
Upload to TestPyPI:
twine upload --repository testpypi dist/*

Install from TestPyPI:
pip install --index-url https://test.pypi.org/simple/ signal_ICT_Kenil_parekh_92400133150

# Example Usage
import numpy as np
import matplotlib.pyplot as plt
from signal_ICT_Kenil_parekh_92400133150.trigonometric_signals import sine_wave

t=np.linspace(0,1,500)
y=sine_wave(2,5,0,t)
plt.plot(t,y)
plt.title("Sine Wave")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

# Expected Outputs
1. Unit step and impulse signals (length 20)  
2. Sine wave (A=2, f=5 Hz, phase=0, t=0–1s)  
3. Shifted sine wave (+5 units)  
4. Addition of step + ramp  
5. Multiplication of sine and cosine  

# Student Information
Name: Kenil Parekh  
Enrollment No: 92400133150
Division: 3EK1