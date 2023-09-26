# import libraries
import numpy as np
import matplotlib.pyplot as plt
        
def driver():

  f = lambda x: (x**6)-x- 1
  fp = lambda x: 6*(x**5)-1
  p0 = 2

  Nmax = 100
  tol = 1e-13

  (p,pstar,info,it) = newton(f,fp,p0,tol, Nmax)
  print('the approximate root is', '%16.16e' % pstar)
  print('the error message reads:', '%d' % info)
  print('Number of iterations:', '%d' % it)

  print(abs((p - pstar)))
  xk = abs((p - pstar))[0:it-1]
  xkp1 = abs((p - pstar))[1:it]

  print("Slope = ", (xk[5]-xk[1])/(xkp1[5]-xkp1[1]))

  plt.plot(xk, xkp1)
  plt.xscale('log')
  plt.yscale('log')
  plt.show()

def newton(f,fp,p0,tol,Nmax):
  """
  Newton iteration.
  
  Inputs:
    f,fp - function and derivative
    p0   - initial guess for root
    tol  - iteration stops when p_n,p_{n+1} are within tol
    Nmax - max number of iterations
  Returns:
    p     - an array of the iterates
    pstar - the last iterate
    info  - success message
          - 0 if we met tol
          - 1 if we hit Nmax iterations (fail)
     
  """
  p = np.zeros(Nmax+1)
  p[0] = p0
  for it in range(Nmax):
      p1 = p0-f(p0)/fp(p0)
      p[it+1] = p1
      if (abs(p1-p0) < tol):
          pstar = p1
          info = 0
          return [p,pstar,info,it]
      p0 = p1
  pstar = p1
  info = 1
  return [p,pstar,info,it]
        
driver()
