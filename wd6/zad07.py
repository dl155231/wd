import numpy as np

def foo(n):
    matrix=np.diag([2 for a in range(n)])
    for i in range(1, n):
        a=np.diag([2*(i+1) for a in range(n-i)],+i)
        b=np.diag([2*(i+1) for a in range(n-i)],-i)
        matrix=matrix+a+b
    return matrix
print(foo(6))
