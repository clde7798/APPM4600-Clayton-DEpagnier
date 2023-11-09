import numpy as np
from scipy import integrate

def compTrap(xint, yint):
    Tn = 0
    for i in range(len(xint) - 1):
        Tn += (yint[i] + yint[i+1])*(xint[i+1]-xint[i]) / 2

    return Tn

def compSimp(xint, yint):
    Sn = 0
    h = xint[1] - xint[0]
    for i in range(0, len(xint) - 2, 2):
        Sn += (yint[i] + 4*yint[i+1] + yint[i+2])*(h/3)
    return Sn

f = lambda x: 1/(1+x**2)
#f = lambda x: x**3

a = -5
b = 5
n1 = 1291
n2 = 109

xint = np.linspace(a,b, n1)
yint = f(xint)

xint2 = np.linspace(a,b, n2)
yint2 = f(xint2)

print(compTrap(xint, yint))
print(compSimp(xint2, yint2))

print(integrate.quad(f, a, b, epsabs=10**-4, full_output=1))
print(integrate.quad(f, a, b, full_output=1))