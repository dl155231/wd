import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 31, 0.1)
s = np.sin(x)
c = np.cos(x)
plt.plot(x, s, 'b-', label='f(x)=sin(x)')
plt.plot(x, c, 'r-', label='f(x)=cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.axis([0, 31, -1.25, 1.25])
plt.legend(loc='upper right')
plt.show()
