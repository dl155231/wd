import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1, 20, 20)
print(x)
plt.plot(x, 1/x, ':>g', label='f(x)=1/x')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.axis([1, len(x), 0, 1])
plt.show()
