import numpy as np

t = np.linspace(0, np.pi, 30)
y = np.cos(t)

N = len(t)

tempSum = 0
for k in range(N):
    tempSum += (t[k] * y[k])

print("the sum is: ", tempSum)