import numpy as np

a = np.arange(81).reshape(9,9)
print(a)
b=a.ravel()
print(b)
c=a.T #transpozycja
print(c)