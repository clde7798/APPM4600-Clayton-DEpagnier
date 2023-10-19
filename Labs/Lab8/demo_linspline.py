from asyncio import Condition
import matplotlib.pyplot as plt
import numpy as np
import math
from numpy.linalg import inv 


def driver():
    
    f = lambda x: 1/(1+(10*x)**2)
    a = -1
    b = 1
    
    ''' create points you want to evaluate at'''
    Neval = 1000
    xeval =  np.linspace(a,b,Neval)
    
    ''' number of intervals'''
    Nint = 10
    '''evaluate the linear spline'''
    #yeval = eval_lin_spline(xeval,Neval,a,b,f,Nint)
    yeval = eval_cubic_spline(xeval,Neval,a,b,f,Nint)
    
    ''' evaluate f at the evaluation points'''
    fex = np.zeros(Neval)
    for j in range(Neval):
      fex[j] = f(xeval[j]) 
      
    
    plt.figure()
    plt.plot(xeval,fex,'ro-')
    plt.plot(xeval,yeval,'bs-')
    plt.legend()
    plt.show 
     
    err = abs(yeval-fex)
    plt.figure()
    plt.plot(xeval,err,'ro-')
    plt.show() 

def find_m(N, y, x):
    N+=1
    mat = np.zeros((N,N))
    ymat = np.zeros(N)
    for i in range(N):
        for j in range(N):
            if (i == j):
                mat[i][j] = 1/3
                if (j != 0):
                    mat[i][j-1] = 1/12
                if (j != N-1):
                    mat[i][j+1] = 1/12
        if (i > 0 and i < N-1):
            h = x[i] - x[i-1]
            ymat[i] = (y[i+1] - 2*y[i] + y[i-1]) / (2*h**2)
    return inv(mat) @ ymat

def cubic_eval(mi, mip1,xi, xip1, fxi, fxip1, x):
    hi = xip1 - xi
    C = (fxi/hi) - ((hi/6)*mi)
    D = (fxip1/hi) - (hi*mip1)/6
    return ((xip1-x)**3)*mi/(6*hi) + ((x-xi)**3)*mip1 / (6*hi) + C*(xip1-x)+D*(x-xi)

def line_eval(x0, fx0, x1, fx1, xeval):
    m = (fx1-fx0) / (x1-x0)
    return m*(xeval-x0)+fx0    
    
def  eval_lin_spline(xeval,Neval,a,b,f,Nint):

    '''create the intervals for piecewise approximations'''
    xint = np.linspace(a,b,Nint+1)
   
    '''create vector to store the evaluation of the linear splines'''
    yeval = np.zeros(Neval) 
    

    for jint in range(Nint):
        '''find indices of xeval in interval (xint(jint),xint(jint+1))'''
        '''let ind denote the indices in the intervals'''
        '''let n denote the length of ind'''
        ind = np.where((xeval > xint[jint]) & (xeval < xint[jint+1]))
        n = len(ind[0])
        '''temporarily store your info for creating a line in the interval of 
         interest'''
        a1= xint[jint]
        fa1 = f(a1)
        b1 = xint[jint+1]
        fb1 = f(b1)
        
        
        for kk in range(n):
           yeval[ind[0][kk]] = line_eval(a1, fa1, b1, fb1, xeval[ind[0][kk]])
           '''use your line evaluator to evaluate the lines at each of the points 
           in the interval'''
           '''yeval(ind(kk)) = call your line evaluator at xeval(ind(kk)) with 
           the points (a1,fa1) and (b1,fb1)'''
    return yeval    

def  eval_cubic_spline(xeval,Neval,a,b,f,Nint):

    '''create the intervals for piecewise approximations'''
    xint = np.linspace(a,b,Nint+1)
   
    '''create vector to store the evaluation of the linear splines'''
    yeval = np.zeros(Neval) 
    M = find_m(Nint, f(xeval), xeval)

    for jint in range(Nint):
        '''find indices of xeval in interval (xint(jint),xint(jint+1))'''
        '''let ind denote the indices in the intervals'''
        '''let n denote the length of ind'''
        ind = np.where((xeval > xint[jint]) & (xeval < xint[jint+1]))
        n = len(ind[0])

        '''temporarily store your info for creating a line in the interval of 
         interest'''
        a1= xint[jint]
        fa1 = f(a1)
        b1 = xint[jint+1]
        fb1 = f(b1)
        m0 = M[jint]
        m1 = M[jint+1]
        
        
        for kk in range(n):
           yeval[ind[0][kk]] = cubic_eval(m0, m1, a1, b1, fa1, fb1, xeval[ind[0][kk]])
           '''use your line evaluator to evaluate the lines at each of the points 
           in the interval'''
           '''yeval(ind(kk)) = call your line evaluator at xeval(ind(kk)) with 
           the points (a1,fa1) and (b1,fb1)'''
    return yeval        
           
if __name__ == '__main__':
      # run the drivers only if this is called from the command line
      driver()               
