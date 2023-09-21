# import libraries
import numpy as np
    
def driver():

# test functions 
     #f1 = lambda x: -1*np.sin(2*x)+5*x/4 - 3/4
     f1 = lambda x: np.sqrt(10/(x+4))
# fixed point is alpha1 = 1.4987....

     #f2 = lambda x: x-((x**5-7) / (5*x**4))
#fixed point is alpha2 = 3.09... 

     Nmax = 100
     tol = 1e-10

# test f1 '''
     x0 = 1.5
     [xstar,ier, vec] = fixedpt(f1,x0,tol,Nmax)
     print('the approximate fixed point is:',xstar)
     print('f1(xstar):',f1(xstar))
     print('Error message reads:',ier)
     print(vec)
     [order, rate] = convergenceOrder(vec, xstar)
     print(order, rate)
     aitkenVec = aitken(vec, tol, Nmax)
     print(aitkenVec)
     [order, rate] = convergenceOrder(aitkenVec, xstar)
     print(order, rate)

     xstar, vec = steffenson(f1, x0, tol, Nmax)
     print(xstar, vec)

     
    
#test f2 '''
'''
     x0 = 1
     [xstar,ier] = fixedpt(f2,x0,tol,Nmax)
     print('the approximate fixed point is:',xstar)
     print('f2(xstar):',f2(xstar))
     print('Error message reads:',ier)

     print("Function c, and d work, but a and b returns an error because the function just grows to infinity")
     print("Only the functions that have a smaller growth work, and only for certain intervals")
'''

# define routines
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
               return [xstar,ier, np.array(vec)]
          x0 = x1

     xstar = x1
     ier = 1
     print(count)
     return [xstar, ier, np.array(vec)]
    

def convergenceOrder(vec, p):
    vec -= p
    n1 = vec[0]
    diff = []
    for i in range(len(vec)-1):
          n2 = vec[i+1]
          diff.append(abs(n2 / n1))
          n1 = n2
    diff = diff[1:-1]
    #print(diff)
    for i in range(len(diff)-1):
        lam = diff[i]
        lam2 = diff[i+1]
        if lam / lam2 <= 1-(10**-2):
             return [-1, diff[0]]
    return [1, diff[0]]

def aitken(approx, tol, maxN):
     pHat = []
     for i in range(len(approx)-2):
          pn = approx[i]
          pn1 = approx[i+1]
          pn2 = approx[i+2]
          pHat.append(pn - (((pn1-pn)**2)/(pn2-2*pn1+pn)))
     return(np.array(pHat))

def steffenson(f, x0, tol, Nmax):
     a = x0
     b = f(a)
     c = f(b)
     vec = []
     for i in range(Nmax):
          vec.append(a)
          pn1 = a - ((b-a)**2)/(c-2*b+a)
          if (abs(pn1-a) < tol):
               return (a, vec)
          a = pn1
          b = f(a)
          c = f(b)
     return

driver()