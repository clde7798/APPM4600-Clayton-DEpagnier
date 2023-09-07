import numpy as np
import numpy.linalg as la
import math
import matplotlib.pyplot as plt
import time

def driver():

     n = 2
     x = np.linspace(1,2,n)


# this is a function handle.  You can use it to define 
# functions instead of using a subroutine like you 
# have to in a true low level language.     
     f = lambda x: x
     g = lambda x: (((-1)**x) /x)

     y = f(x)
     w = g(x)


# evaluate the dot product of y and w     
     dp = dotProduct(y,w,n)

# print the output
     print('the dot product is : ', dp)
     # This is my two matrices
     mat1 = np.array([1,3, 4,2]).reshape(2,2)
     mat2 = np.array([1,2, 2,3]).reshape(2,2)

     start1 = time.time()
     newMat = matrixMult(mat1, mat2, 2)
     end1 = time.time()
     print ("The new matrix is: \n", newMat)
     print('Run time: ', end1-start1)
     print()
     print()

     npDot = np.dot(y,w)

     start2 = time.time()
     npMatMult = np.matmul(mat1, mat2)
     end2 = time.time()

     print('The built-in dot product is: ', npDot)
     print('The built-in matrix mult gives: \n', npMatMult)
     print('Run time: ', end2-start2)
     print()

     print('Looks like they are both working well!')

     return
     
def dotProduct(x,y,n):

     dp = 0.
     for j in range(n):
        dp = dp + x[j]*y[j]

     return dp

def matrixMult(x,y,n):
     mat = np.zeros((n,n))
     for i in range(n):
          for j in range(n):
               mat[i,j] = dotProduct(x[i], y[:,j], n)
     return mat

driver()               
