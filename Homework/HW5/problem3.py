import numpy as np

def f(x,y,z):
    return (x**2+4*y**2+4*z**2-16)

def fx(x):
    return (2*x)

def fy(y):
    return (8*y)

def fz(z):
    return (8*z)

x0 = 1
y0 = 1
z0 = 1

xn = x0
yn = x0
zn = x0

xit = [1]
yit = [1]
zit = [1]


while (f(xn,yn,zn) != 0):
    d = f(x0,y0,z0) / (fx(x0)**2+fy(y0)**2+fz(z0)**2)
    xn = x0 - d*fx(x0)
    yn = y0 - d*fy(y0)
    zn = z0 - d*fz(z0)

    xit.append(xn)
    yit.append(yn)
    zit.append(zn)
    

    x0  = xn
    y0 = yn
    z0 = zn

xit = np.array(xit)
yit = np.array(yit)
zit = np.array(zit)

its = len(xit)
error = xit - xit[-1]

print("Point on Surface (x,y,z): ")
print([xit[-1], yit[-1],zit[-1]])
print()
print("X Error per iteration: ")
print(abs(error[1:its-1]/(error[0:its-2])))

error = yit - yit[-1]
print("Y Error per iteration: ")
print(abs(error[1:its]/(error[0:its-1])))

error = zit - zit[-1]
print("Z Error per iteration: ")
print(abs(error[1:its]/(error[0:its-1])))
print()
print("So we can see that the iteration converges Quadratically since if you square the error value for each X, Y, and Z array it equals the next value.")
