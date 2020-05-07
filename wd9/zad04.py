import pandas as pd
import matplotlib.pyplot as plt

# wczytanie danych datasetu
iris = pd.read_csv('iris.csv', sep=',')

# legenda wykresu
colors = ['red', 'green', 'blue']
gatunki = iris['species'].unique()


for i in range(0, 3):
    gatunki_df = iris[iris['species'] == gatunki[i]]
    plt.scatter(
        gatunki_df['sepal_length'],
        gatunki_df['sepal_width'],
        color=colors[i],
        alpha=0.7,
        label=gatunki[i]
    )

plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')
plt.legend()

plt.show()
