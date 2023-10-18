import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt

def driver():


    f = lambda x: 1/(1+(10*x)**2)

    N = 20
    ''' interval'''
    a = -1
    b = 1
    h = 2/(N-1)
   
    ''' create equispaced interpolation nodes'''
    #xint = np.linspace(a,b,N+1)
    #xint = np.array([-1+(i-1)*h for i in range(1,N+2)])
    xint = np.array([np.cos((2*i - 1)*np.pi / (2*N)) for i in range(1, N+2)])
    
    ''' create interpolation data'''
    yint = f(xint)
    
    ''' create points for evaluating the Lagrange interpolating polynomial'''
    Neval = 1001
    xeval = np.linspace(a,b,Neval+1)
    yeval_l= np.zeros(Neval+1)
    yeval_dd = np.zeros(Neval+1)
    yeval_bary = np.zeros(Neval+1)
  
    '''Initialize and populate the first columns of the 
     divided difference matrix. We will pass the x vector'''
    y = np.zeros( (N+1, N+1) )
     
    for j in range(N+1):
       y[j][0]  = yint[j]

    y = dividedDiffTable(xint, y, N+1)
    ''' evaluate lagrange poly '''
    for kk in range(Neval+1):
       yeval_l[kk] = eval_lagrange(xeval[kk],xint,yint,N)
       yeval_dd[kk] = evalDDpoly(xeval[kk],xint,y,N)
       yeval_bary[kk] = eval_barycentric(xeval[kk], xint, yint, N)

    yeval_m = monomial(N,xint,yint, xeval)



    ''' create vector with exact values'''
    fex = f(xeval)
       

    plt.figure()    
    plt.plot(xeval,fex,'ro-', label = "f(x)")
    #plt.plot(xeval,yeval_l,'co-', label='lagrange') 
    plt.plot(xeval,yeval_bary,'bo-', label='barycentric') 
    #plt.plot(xeval,yeval_dd,'c.--')
    #plt.plot(xeval, yeval_m, 'o', color='black', label = "Monomial")
    plt.title(f'Function vs Barycentric: N = {N}')
    plt.legend()

    plt.figure() 
    err_l = abs(yeval_l-fex)
    err_bary = abs(yeval_bary-fex)
    err_dd = abs(yeval_dd-fex)
    err_m = abs(yeval_m-fex)
    #plt.semilogy(xeval,err_l,'co--',label='lagrange')
    plt.semilogy(xeval,err_bary,'bo-',label='barycentric')
    #plt.semilogy(xeval,err_dd,'bs--',label='Newton DD')
    #plt.semilogy(xeval,err_m,'o', color='black',label='Monomial')
    plt.title(f'Barycentric Error: N = {N}')
    plt.legend()
    plt.show()


def monomial(N, xint, yint , x):
   N+=1
   van = np.zeros((N,N))
   for i in range(N):
      for j in range(N):
         van[i][j] = xint[i]**j
   invVan = la.inv(van)
   coefs = invVan @ yint
   px = 0
   for i in range(N):
      px += x**i * coefs[i]
   return px

      

def eval_lagrange(xeval,xint,yint,N):

    lj = np.ones(N+1)
    
    for count in range(N+1):
       for jj in range(N+1):
           if (jj != count):
              lj[count] = lj[count]*(xeval - xint[jj])/(xint[count]-xint[jj])

    yeval = 0.
    
    for jj in range(N+1):
       yeval = yeval + yint[jj]*lj[jj]
    return(yeval)
  
def eval_barycentric(xeval,xint,yint,N):
    wj = np.ones(N+1)
    for i in range(N+1):
       for j in range(N+1):
           if (j != i):
            wj[i] = (wj[i]*(xint[i]-xint[j]))
    wj = 1/ wj
    num = 0
    denom = 0
    for j in range(N+1):
       if (xeval != xint[j]):
         num += wj[j]*yint[j] / (xeval-xint[j])
         denom += wj[j] / (xeval-xint[j])
    yeval = num / denom
    return(yeval)  
  

''' create divided difference matrix'''
def dividedDiffTable(x, y, n):
 
    for i in range(1, n):
        for j in range(n - i):
            y[j][i] = ((y[j][i - 1] - y[j + 1][i - 1]) /
                                     (x[j] - x[i + j]))
    return y
    
def evalDDpoly(xval, xint,y,N):
    ''' evaluate the polynomial terms'''
    ptmp = np.zeros(N+1)
    
    ptmp[0] = 1.
    for j in range(N):
      ptmp[j+1] = ptmp[j]*(xval-xint[j])
     
    '''evaluate the divided difference polynomial'''
    yeval = 0.
    for j in range(N+1):
       yeval = yeval + y[0][j]*ptmp[j]  

    return yeval

       

driver()        
