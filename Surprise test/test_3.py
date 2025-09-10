#Create an array of numbers 1–100 and reshape it into a 10×10 matrix. Then, extract all prime numbers.

import numpy as np
array=np.arange(1,101)
matrix=array.reshape(10,10)
print(matrix)
def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
primes=array[[is_prime(x) for x in array]]
print("\nPrime No:\n",primes)

