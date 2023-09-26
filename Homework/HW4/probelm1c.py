# import libraries
import numpy as np
import scipy.integrate as integrate
        
def driver():
  alpha = 0.138 * 10**-6
  t = 3600*60*24

  f = lambda x: -15/35 + (2/np.sqrt(np.pi))*integrate.quad(lambda s: np.exp(-s**2), 0 ,(x/(2*np.sqrt(t*alpha))))[0]
  fp = lambda x: (1/(np.sqrt(np.pi)*np.sqrt(alpha*t)))*np.exp(-1*((x**2)/(4*alpha*t)))
  p0 = 2

  Nmax = 100
  tol = 1e-13

  (p,pstar,info,it) = newton(f,fp,p0,tol, Nmax)
  print('the approximate root is', '%16.16e' % pstar)
  print('the error message reads:', '%d' % info)
  print('Number of iterations:', '%d' % it)


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
