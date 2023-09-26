# import libraries
import numpy as np
import matplotlib.pyplot as plt
        
def driver():

  f = lambda x: (x**6)-x- 1
  p0 = 2
  p1 = 1

  Nmax = 100
  tol = 1e-13

  (p,pstar,info,it) = secant(f,p0, p1, tol, Nmax)
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

def secant(f,p0,p1,tol,Nmax):
    p = np.zeros(Nmax+1)
    p[0] = p0
    if (f(p0) == 0):
        return [p,p0,0,0]
    if(f(p1) == 0):
        return [p, p1, 0, 0]
    fp1 = f(p1)
    fp0 = f(p0)

    for it in range(Nmax):
        if(fp0-fp1 == 0):
            return [p,p1,1,it]
        p2 = p1 - (fp1*(p1-p0))/(fp1-fp0)
        if abs(p2-p1) < tol:
            pstar = p1
            info = 0
            return [p,pstar, info, it+1]
        p0 = p1
        fp0 = fp1
        p1 =p2
        fp1 = f(p2)
        p[it+1] = p0
    pstar = p2
    info = 1
    return[p,pstar,info, it+1]

driver()
