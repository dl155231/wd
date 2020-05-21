import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_excel('imiona.xlsx')
plt.figure(figsize=(15, 6))
plt.subplots_adjust(wspace=0.27)


# wykres 1
plt.subplot(131)

tmp1 = df.groupby(df['Plec']).agg({'Liczba': ['sum']})

etykiety1 = ['K', 'M']
wartosci1 = tmp1['Liczba'].values.reshape(2)

plt.bar(etykiety1, wartosci1, color=['#FFBFCA', '#0000F2'])
plt.title('Narodziny w całym okresie (mln)')
plt.xlabel('Plec')
plt.ylabel('Ilość narodzin')


# wykres 2
plt.subplot(132)

tmp2 = df.groupby(['Plec', 'Rok']).agg({'Liczba': ['sum']})
etykiety2 = [x for x in range(2000, 2018)]
wartosci2 = tmp2['Liczba'].values.reshape(18, 2)

plt.plot(etykiety2, wartosci2)
plt.title('Narodziny ze względu na płeć')
plt.xlabel('Rok')
plt.ylabel('Ilość narodzin')
plt.xticks(etykiety2, rotation=45)
plt.legend(['Mezczyzni', 'Kobiety'])

# wykres 3
plt.subplot(133)

tmp3 = df.groupby(['Rok']).agg({'Liczba': ['sum']})

etykiety3 = [x for x in range(2000, 2018)]
wartosci3 = tmp3['Liczba'].values.reshape(18)

kolory = ['#FF0000', '#FD4B02', '#FB9405', '#F9DA08', '#D2F80B', '#8EF60D', '#4CF410', '#13F319', '#15F15B',
          '#18EF9A', '#1AEDD8', '#1DC5EC', '#1F8AEA', '#2150E8', '#2E24E7', '#6826E5', '#9F28E3', '#D32AE2']

plt.bar(etykiety3, wartosci3, color=kolory)
plt.title('Sumaryczna liczba narodzin w każdym roku')
plt.xlabel('Rok')
plt.ylabel('Ilość narodzin')
plt.xticks(etykiety3, rotation=45)

plt.show()

