import pandas as pd

df = pd.read_csv('datasets/zamowienia.csv', sep=';')

# 3a
#print(df['Sprzedawca'].unique())

# 3b
#df2=df.nlargest(5, ['Utarg'])
#print(df2['Utarg'])

# 3c
#print(df.groupby(df['Sprzedawca']).agg({'idZamowienia':['count']}))

# 3d
#print(df.groupby(df['Kraj']).agg({'idZamowienia':['count']}))

# 3e
#print(df.loc[((df['Kraj']=='Polska') & (df['Data zamowienia']<'2006-01-01')) & (df['Data zamowienia']>'2004-12-31'), 'idZamowienia'].count())

# 3f
#print(df.loc[((df['Data zamowienia']<'2005-01-01')) & (df['Data zamowienia']>'2003-12-31'), 'idZamowienia'].mean())
dane1 = df.loc[((df['Data zamowienia']<'2005-01-01')) & (df['Data zamowienia']>'2003-12-31')]
dane2 = df.loc[((df['Data zamowienia']<'2006-01-01')) & (df['Data zamowienia']>'2004-12-31')]
dane1.to_csv('datasets/zamowienia_2004.csv')
dane2.to_csv('datasets/zamowienia_2005.csv')