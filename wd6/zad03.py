import numpy as np

def foo(n):
    a=np.arange(1, n*n+1, 1)
    return a
print(foo(9))
