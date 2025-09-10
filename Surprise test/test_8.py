#Replace all even numbers in an array with -1.

import numpy as np
array=np.arange(1,21)
print(array)
array[array%2==0]= -1
print(array)
