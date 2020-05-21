import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('imiona.xlsx')

tmp2 = df.groupby(['Plec', 'Rok']).agg({'Liczba': ['sum']})

etykiety = [x for x in range(2000, 2018)]
wartosci = tmp2['Liczba'].values.reshape(2, 18)

K = wartosci[0][:]
M = wartosci[1][:]

plt.figure(figsize=(15, 6))
plt.bar(etykiety, K, color='red', label='kobiety')
plt.bar(etykiety, M, color='blue', label='mezczyzni', bottom=K)

plt.title('Narodziny ze względu na płeć')
plt.xlabel('Rok')
plt.ylabel('Ilość narodzin')
plt.xticks(etykiety, rotation=45)
plt.show()
