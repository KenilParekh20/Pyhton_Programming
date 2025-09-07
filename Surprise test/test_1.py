#Create a 5×5 matrix with values 1,2, 3,….25 and extract the border elements into a 1D array

import numpy as np
matrix=np.arange(1,26).reshape(5,5)
print(matrix)
border=np.concatenate([matrix[0,:],      
                       matrix[1:-1,-1],    
                       matrix[-1,::-1],   
                       matrix[-2:0:-1,0]])
print(border)
