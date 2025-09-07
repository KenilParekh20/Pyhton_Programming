#Construct a 1D NumPy array of length 100, and replace every 5th element with -1.

import numpy as np
array=np.arange(1,101)
array[4::5]=-1
print(array)