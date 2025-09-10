#Create a 5×5 matrix and set the border elements to 1 and inner elements to 0.

import numpy as np
matrix=np.ones((5,5),dtype=int)
matrix[1:-1,1:-1]=0
print(matrix)
