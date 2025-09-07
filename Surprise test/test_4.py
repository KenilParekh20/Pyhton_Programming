#Verify the Pythagorean identity: sin²θ + cos²θ = 1 for θ = [0, 30, 45, 60, 90] degrees.

import numpy as np
angles=[0,30,45,60,90]
for angle in angles:
 rad = np.radians(angle)         
 total=np.sin(rad)**2+np.cos(rad)**2  # sin²θ + cos²θ
 print(angle,"degrees =",total)
