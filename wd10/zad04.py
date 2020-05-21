import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 31, 0.1)
s = np.sin(x)
plt.plot(x, s+2, label='sin(x)')
plt.plot(x, -s, color='#FF8C00', label='sin(x)')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.axis([-1, 30, -1.25, 3.25])
plt.legend(loc='center left')
plt.show()
