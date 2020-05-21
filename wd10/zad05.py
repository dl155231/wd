import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
np.random.seed(19991205)
iris = pd.read_csv('iris.csv', sep=',')
x = iris['sepal_length']
y = iris['sepal_width']
kolory = np.random.randint(0, 50, 150)
plt.scatter(x, y, label='wykres punktowy', c=kolory,
            s=np.abs(iris['sepal_length']-iris['sepal_width'])*10)
plt.show()
