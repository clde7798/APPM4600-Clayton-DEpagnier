import math

x = 9.999999995000000*10**-10
y = math.e**x - 1

print("math.e^x -1: ", y)
print("8 correct digits.")

t2 = x+(x**2)/2
print('Tayler Polynomial evaluated with x: ', t2)
print('Relative Error of T2: ', abs(10**-9 - t2) / abs(t2))