import numpy as np

def foo(n):
    a=np.diag([n for n in range(n, 0, -1)])
    return a
print(foo(6))
