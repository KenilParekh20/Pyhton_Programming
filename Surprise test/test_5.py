#Create a 3×3 matrix with values 1–9 and compute the reciprocal (1/x) of each element.

import numpy as np
a1=np.arange(1,10).reshape(3,3)
print(a1)
reciprocal=1/a1
print("\nReciprocal:",reciprocal)