Timer unit: 1e-06 s

Total time: 0.001451 s
File: matmult_modifed.py
Function: MultiX at line 4

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     4                                           @profile
     5                                           def MultiX(n):
     6         1          2.0      2.0      0.1   N = n
     7
     8         1         14.0     14.0      1.0   X = np.arange(N,dtype='int')
     9         1          4.0      4.0      0.3   Y = np.arange(N+1,dtype='int')
    10
    11         1       1431.0   1431.0     98.6   print(np.outer(X, Y))


