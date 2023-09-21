import numpy as np
import matplotlib.pyplot as plt

f = lambda x: x - 4*np.sin(2*x)-3

xvals = np.linspace(6.5,7.5,100)
yvals = [f(x) for x in xvals]

plt.plot(xvals, yvals)
plt.plot([6.5,7.5], [0,0])
plt.show()