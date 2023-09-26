import scipy
import numpy as np
import matplotlib.pyplot as plt


def driver():

# use routines
    alpha = 0.138 * 10**-6
    t = 3600*60*24

    f = lambda x: -1*(15/35 - (2/np.sqrt(np.pi))*scipy.integrate.quad(lambda s: np.exp(-s**2), 0 ,(x/(2*np.sqrt(t*alpha))))[0])
    a = 0
    b = 1


    tol = 1e-13

    [astar,ier] = bisection(f,a,b,tol)
    print('the approximate root is',astar)
    print('the error message reads:',ier)
    print('f(astar) =', f(astar))






# define routines
def bisection(f,a,b,tol):

    fa = f(a)
    fb = f(b)
    if (fa*fb>0):
       ier = 1
       astar = a
       return [astar, ier]

#   verify end points are not a root 
    if (fa == 0):
      astar = a
      ier =0
      return [astar, ier]

    if (fb ==0):
      astar = b
      ier = 0
      return [astar, ier]

    count = 0
    d = 0.5*(a+b)
    while (abs(d-a)> tol):
      fd = f(d)
      if (fd ==0):
        astar = d
        ier = 0
        return [astar, ier]
      if (fa*fd<0):
         b = d
      else: 
        a = d
        fa = fd
      d = 0.5*(a+b)
      count = count +1
#      print('abs(d-a) = ', abs(d-a))
      
    astar = d
    ier = 0
    return [astar, ier]
      
driver()               
