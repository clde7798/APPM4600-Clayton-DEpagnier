import matplotlib.pyplot as plt
import numpy as np
import math
from numpy.linalg import inv 
from numpy.linalg import norm


def driver():
    
    f = lambda x: 1/(1+x**2)
    fp = lambda x: -2*x/(1+x**2)**2

    a = -5
    b = 5
    
    ''' create points you want to evaluate at'''
    Neval = 100
    xeval =  np.linspace(a,b,Neval+1)
    
    ''' number of intervals'''
    Nint = 20
    #xint = np.linspace(a,b,Nint+1)
    xint = np.array([5*np.cos((i)*np.pi / Nint) for i in range(Nint+1)])
    xint = np.flip(xint)

    yint = f(xint)
    yintp = fp(xint)
    
    (M,C,D) = create_natural_spline(yint,xint,Nint)
    (M2,C2,D2) = create_clamped_spline(yint,xint,Nint, yintp)
    
    print('M =', M)
#    print('C =', C)
#    print('D=', D)
    
    yeval = eval_cubic_spline(xeval,Neval,xint,Nint,M,C,D)
    yeval2 = eval_cubic_spline(xeval,Neval,xint,Nint,M2,C2,D2)
    
#    print('yeval = ', yeval)
    
    ''' evaluate f at the evaluation points'''
    fex = f(xeval)
        
    nerr = norm(fex-yeval)
    print('nerr = ', nerr)
    
    plt.figure()    
    plt.plot(xeval,fex,'ro-',label='exact function')
    plt.plot(xeval,yeval,'bs--',label='natural spline')
    plt.plot(xeval,yeval2,'c--',label='clamped spline') 
    plt.legend()
    plt.show()
    

    err = abs(yeval-fex)
    err2 = abs(yeval2-fex)
    plt.figure() 
    plt.semilogy(xeval,err,'ro--',label='absolute error Natural')
    plt.semilogy(xeval,err2,'bo--',label='absolute error Clamped')
    plt.legend()
    plt.show()

def create_clamped_spline(yint,xint,N, yintp):

#    create the right  hand side for the linear system
    b = np.zeros(N+1)
#  vector values
    h = np.zeros(N+1)  
    for i in range(1,N):
       hi = xint[i]-xint[i-1]
       hip = xint[i+1] - xint[i]
       b[i] = (yint[i+1]-yint[i])/hip - (yint[i]-yint[i-1])/hi
       h[i-1] = hi
       h[i] = hip

    b[0] = -yintp[0] + ((yint[1]-yint[0]) / h[0])
    b[N] = -yintp[N] + ((yint[N]-yint[N-1]) / h[N-1])
#  create matrix so you can solve for the M values
# This is made by filling one row at a time 
    A = np.zeros((N+1,N+1))
    A[0][0] = h[0] / 3
    A[0][1] = h[0] / 6
    for j in range(1,N):
       A[j][j-1] = h[j-1]/6
       A[j][j] = (h[j]+h[j-1])/3 
       A[j][j+1] = h[j]/6
    A[N][N-1] = h[N-1] / 6
    A[N][N] = h[N-1] / 3  

    Ainv = inv(A)
    
    M  = Ainv.dot(b)

#  Create the linear coefficients
    C = np.zeros(N)
    D = np.zeros(N)
    for j in range(N):
       C[j] = yint[j]/h[j]-h[j]*M[j]/6
       D[j] = yint[j+1]/h[j]-h[j]*M[j+1]/6
    return(M,C,D)
    
def create_natural_spline(yint,xint,N):

#    create the right  hand side for the linear system
    b = np.zeros(N+1)
#  vector values
    h = np.zeros(N+1)  
    for i in range(1,N):
       hi = xint[i]-xint[i-1]
       hip = xint[i+1] - xint[i]
       b[i] = (yint[i+1]-yint[i])/hip - (yint[i]-yint[i-1])/hi
       h[i-1] = hi
       h[i] = hip

#  create matrix so you can solve for the M values
# This is made by filling one row at a time 
    A = np.zeros((N+1,N+1))
    A[0][0] = 1.0
    for j in range(1,N):
       A[j][j-1] = h[j-1]/6
       A[j][j] = (h[j]+h[j-1])/3 
       A[j][j+1] = h[j]/6
    A[N][N] = 1

    Ainv = inv(A)
    
    M  = Ainv.dot(b)

#  Create the linear coefficients
    C = np.zeros(N)
    D = np.zeros(N)
    for j in range(N):
       C[j] = yint[j]/h[j]-h[j]*M[j]/6
       D[j] = yint[j+1]/h[j]-h[j]*M[j+1]/6
    return(M,C,D)
       
def eval_local_spline(xeval,xi,xip,Mi,Mip,C,D):
# Evaluates the local spline as defined in class
# xip = x_{i+1}; xi = x_i
# Mip = M_{i+1}; Mi = M_i

    hi = xip-xi
    yeval = (Mi*(xip-xeval)**3 +(xeval-xi)**3*Mip)/(6*hi) \
            + C*(xip-xeval) + D*(xeval-xi)
    return yeval 
    
    
def  eval_cubic_spline(xeval,Neval,xint,Nint,M,C,D):
    
    yeval = np.zeros(Neval+1)
    
    for j in range(Nint):
        '''find indices of xeval in interval (xint(jint),xint(jint+1))'''
        '''let ind denote the indices in the intervals'''
        atmp = xint[j]
        btmp= xint[j+1]
        
#   find indices of values of xeval in the interval
        ind= np.where((xeval >= atmp) & (xeval <= btmp))
        xloc = xeval[ind]

# evaluate the spline
        yloc = eval_local_spline(xloc,atmp,btmp,M[j],M[j+1],C[j],D[j])
#        print('yloc = ', yloc)
#   copy into yeval
        yeval[ind] = yloc

    return(yeval)
           
driver()               

