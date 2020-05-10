import pandas as pd

df = pd.read_excel('datasets/imiona.xlsx', 'Arkusz1')

# 2a
#print(df[df['Liczba']>1000])

# 2b
#print(df[df['Imie']=='DOMINIK'])

# 2c
#print(df['Liczba'].sum())

# 2d
#print(df.loc[df['Rok'] < 2006, 'Liczba'].sum())

# 2e
#print(df.groupby(df['Plec']).agg({'Liczba':['sum']}))

# 2f
#print(df.sort_values('Liczba', ascending=False).groupby(['Rok','Plec']).nth(0))