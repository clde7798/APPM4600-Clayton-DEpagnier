# import libraries
import numpy as np
        
def driver():

  f = lambda x: x**6-x-1
  fp = lambda x: 6*x**5-1
  fpp = lambda x: 30*x**4

  
  p0 = 100

  Nmax = 100
  tol = 1.e-14

  (p,pstar,info,it) = mod_newton(f,fp,p0,tol, Nmax, 1,1.5)
  print('the approximate root is', '%16.16e' % pstar)
  print('the error message reads:', '%d' % info)
  print('Number of iterations:', '%d' % it)


def mod_newton(f,fp,p0,tol,Nmax, a, b):
  a1 = a
  b1 = b
  fa = f(a)
  fb = f(b)
  g = lambda x: x- f(x)/fp(x)
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
  while (g(d) > b1 or g(d) < a1):
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
  p0 = d
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