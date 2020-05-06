import numpy as np
np.set_printoptions(suppress=True)

def fib(n):
    if n == 0:
        return 0
    else:
        f = np.zeros(n+1)
        f[0] = 0
        f[1] = 1
        for i in range(2, n+1):
            f[i] = f[i-1] + f[i-2]
        return f[n]

A = np.empty(25)
for i in range(0, 25):
    A[i] = fib(i+1)
A = A.reshape(5, 5)
print(A)
