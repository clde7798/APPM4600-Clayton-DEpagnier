import numpy as np

x = np.pi/2
h = np.array([0.01*2**-i for i in range(10)])

f1 = (np.cos(x+h) - np.cos(x))/h
f2 = (np.cos(x+h) - np.cos(x-h))/2*h

print(f1[1:9] / f1[0:8])
print(f2[1:9] / f2[0:8])