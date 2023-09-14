import numpy as np
import matplotlib.pyplot as plt
import random

theta = np.linspace(0, 2*np.pi, 100)

def xFunc(R, deltar, f, p, theta):
    return R*(1+deltar*np.sin(f*theta+p))*np.cos(theta)

def yFunc(R, deltar, f, p, theta):
    return R*(1+deltar*np.sin(f*theta+p))*np.sin(theta)

x = xFunc(1.2,0.1, 15, 0, theta)
y = yFunc(1.2,0.1, 15, 0, theta)

plt.plot(x,y)
plt.axis('equal')
plt.show()


for i in range(10):
    x = xFunc(i, 0.05, 2+i, random.uniform(0,2), theta)
    y = yFunc(i, 0.05, 2+i, random.uniform(0,2), theta)
    plt.plot(x,y)

plt.axis('equal')
plt.show()

