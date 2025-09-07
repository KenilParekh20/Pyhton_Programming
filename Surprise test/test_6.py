#Extract the first row and last column from a 4×4 matrix.

import numpy as np
matrix=np.arange(1,17).reshape(4,4)
print(matrix)
print(matrix[0])
print(matrix[:,3])
