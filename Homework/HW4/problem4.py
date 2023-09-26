# import libraries
import numpy as np
        
def driver():
  m = 3
  #ERROR, MUST FACTOR TO NOT LOSE DIGITS
  #f = lambda x: np.exp(3*x)-(27*(x**6))+(27*((x**4)*np.exp(x)))-(9*(x**2)*np.exp(2*x))
  #fp = lambda x: 3*np.exp(3*x)-162*(x**5)+108*(x**3)*np.exp(x)+27*(x**4)*np.exp(x)-18*x*np.exp(2*x)-18*(x**2)*np.exp(x)
  #fpp = lambda x: 9*np.exp(3*x)-810*(x**4)+27*(x**4)*np.exp(x)+216*(x**3)*np.exp(x)+(324*np.exp(x)*x**2)-(36*np.exp(2*x)*x**2)-(72*np.exp(2*x)*x)-(18*np.exp(2*x))

  f = lambda x: (np.exp(x)-3*x**2)**3
  fp = lambda x: (3*(np.exp(x)-3*x**2)**2)*(np.exp(x)-(6*x))
  fpp = lambda x: (6*(np.exp(x)-(3*x**2))*((np.exp(x)-6*x)**2))+(3*((np.exp(x)-(3*x**2))**2)*(np.exp(x)-6))
  #ii)
  
  f2 = lambda x: f(x) / fp(x)
  fp2 = lambda x: 1-((f(x)*(fpp(x))) / (fp(x)**2))

  #iii)
  f3 = lambda x: x - m*f2(x)


  p0 = 3

  Nmax = 100
  tol = 1e-10

  print("PART i)")
  (p,pstar,info,it) = newton(f,fp,p0,tol, Nmax)
  print('the approximate root is', '%16.16e' % pstar)
  print('the error message reads:', '%d' % info)
  print('Number of iterations:', '%d' % it)
  convergenceOrder(p[0:it], pstar)

  print("PART ii)")
  (p,pstar,info,it) = newton(f2,fp2,p0,tol, Nmax)
  print('the approximate root is', '%16.16e' % pstar)
  print('the error message reads:', '%d' % info)
  print('Number of iterations:', '%d' % it)
  convergenceOrder(p[0:it], pstar)

  print("PART iii)")
  (p,pstar,info,it) = fixedpt(f3,p0,tol, Nmax)
  print('the approximate root is', '%16.16e' % pstar)
  print('the error message reads:', '%d' % info)
  print('Number of iterations:', '%d' % it)
  convergenceOrder(p, pstar)


  
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
        

def fixedpt(f,x0,tol,Nmax):
  vec = []
  ''' x0 = initial guess''' 
  ''' Nmax = max number of iterations'''
  ''' tol = stopping tolerance'''
  count = 0
  while (count <Nmax):
      vec.append(x0)
      count = count +1
      x1 = f(x0)
      if (abs(x1-x0) <tol):
            xstar = x1
            ier = 0
            print(count)
            return [np.array(vec), xstar,ier, count]
      x0 = x1

  xstar = x1
  ier = 1
  print(count)
  return [np.array(vec), xstar,ier, count]
    

def convergenceOrder(vec, p):
  vec -= p
  n1 = vec[0]
  diff = []
  for i in range(len(vec)-1):
        n2 = vec[i+1]
        diff.append(abs(n2 / n1))
        n1 = n2
  diff = diff[1:-1]
  print(diff)
  return

driver()