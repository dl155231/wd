import numpy as np

a=np.arange(9).reshape(3,3)
for i in a.flat:
    print(i)