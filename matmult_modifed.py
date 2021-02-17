# Program to multiply two matrices using Numpy arrays

import numpy as np
@profile
def MultiX(n):
 N = n
 
 X = np.arange(N,dtype='int')
 Y = np.arange(N+1,dtype='int')
 
 print(np.outer(X, Y))

MultiX(250)
