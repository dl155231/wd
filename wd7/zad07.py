import numpy as np

def add(a, b):
    return a+b

sinus=np.array([2, 2, 2, 2, 2, 2]).reshape(2, 3)
a=np.sin(sinus)
cosinus=np.array([4, 4, 4, 4, 4, 4]).reshape(2, 3)
b=np.cos(cosinus)

print(add(a, b))