import numpy as np

def foo(a, direction):
    if(a.shape[0]%2!=0):
        return "nieparzysty rozmiar tablicy"
    else:
        if(direction==1):
            return a[:int(a.shape[0]/2)]
        else:
            return np.hsplit(a, 2)[0]
a=np.arange(16)
a=a.reshape((4,4))
print(foo(a, 0))
