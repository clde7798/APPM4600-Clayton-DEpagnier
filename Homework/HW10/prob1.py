import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as la
import math

def driver():


    f = lambda x: np.sin(x)
    fm = lambda x: x- (x**3)/6 + (x**5)/math.factorial(5)

    p33 =  lambda x: (x-(7/60)*x**3) / (1+(x**2)/20)
    p24 = lambda x: x / (1+(x**2)/6 + (7*x**4)/360)

    N = 30
    ''' interval'''
    a = 0
    b = 5
   
    ''' create equispaced interpolation nodes'''
    xint = np.linspace(a,b,N+1)

    ''' create interpolation data'''
    evalf = f(xint)
    
    evalfm = fm(xint)

    evalp33 = p33(xint)

    evalp24 = p24(xint)
    

         
    errfm = abs(evalf - evalfm)
    errp33 = abs(evalf - evalp33)
    errp24 = abs(evalf - evalp24)

    plt.figure()
    plt.semilogy(xint,errp33,'bs-',label='Pade P33 / P42')
    plt.semilogy(xint,errp24,'rs-',label='Pade P24')
    plt.semilogy(xint,errfm,'c.-',label='6th order Maclaurin')
    plt.legend()
    plt.show()           
    

       
if __name__ == '__main__':
  # run the drivers only if this is called from the command line
  driver()        
