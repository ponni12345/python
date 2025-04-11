from scipy import linalg
import numpy as np

'''3x+y=9
x+2y=8'''

#coefficient matrix(A) and constant vector(b)

A = np.array([[3,1],[1,2]])
b = np.array([9,8])

#solve for x
x=linalg.solve(A,b)
print("solution:")
print("x=",x[0])
print("y=",x[1])
