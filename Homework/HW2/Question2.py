import numpy.linalg as la
import numpy as np


Ainverse = np.matrix([[1-10**10, 10**10], [1 + 10**10, -10**10]])
print('A^-1: \n', Ainverse)
print('Norm of A^-1: ', la.norm(Ainverse))

db1 = 7 * 10**-6
db2 = 3 * 10**-6
deltaX = np.matrix([[db1*(1-10**10)+(10**10)*db2], [db1*(1+10**10)-(10**10)*db2]])
print("B1 = ", db1, "and delta B2 = ", db2)
print('Relative Error of X, ', la.norm(deltaX / np.sqrt(2)))
