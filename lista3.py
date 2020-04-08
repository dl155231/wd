from liczbyZespolone import czesci, dodOdej
import ciagi as c
import math as m
import random as r


# zad.1
A = [1/x for x in range(1, 11)]
B = [2**y for y in range(11)]
C = [z for z in B if z % 4 == 0]
# print(A)
# print(B)
# print(C)


# zad.2
macierz = [[r.randint(0, 11) for x in range(4)] for x in range(4)]
lista = [macierz[index][index] for index in range(4)]
# print(macierz)
# print(lista)


# zad.3
produkty = {
    "ciasto": "kg",
    "cukier": "kg",
    "cytryna": "szt",
    "zapalniczka": "szt",
    "woda": "l"
}
sztuki = [key for key, value in produkty.items() if value == "szt"]
# print(slownik2)


# zad.4
def monFun(a, b):
    if (a > 0):
        return "Funkcja jest rosnaca"
    elif (a == 0):
        return "Funkcja jest stała"
    else:
        return "Funkcja jest malejąca"
# print(mon_fun(-3, 5))


# zad.5
def porFunkcji(a1, b1, a2, b2):
    if (a1 == a2):
        return "Proste są równoległe"
    elif (a1*a2 == -1):
        return "Proste są prostopadłe"


# zad.6
def promienOkregu(x, y, a=0, b=0):
    promien = m.sqrt((x-a)**2+(y-b)**2)
    return promien
# print(promienOkregu(3,3))


# zad.7
def przeciwprostokatna(a=1, b=1):
    return m.sqrt(a**2+b**2)
# print(przeciwprostokatna(5,12))


# zad.8
def sumaCiagu(a1=1, r=1, ile=10):
    return ((2*a1+(ile-1)*r)/2)*ile
# print(sumaCiagu())


# zad.9
def iloczynCiagu(* liczba):
    iloczyn = 1
    if len(liczba) == 0:
        return 0
    else:
        for i in liczba:
            iloczyn *= i
        return iloczyn
# print(iloczynCiagu(1,2,3,4,5))


# zad.10
def zakupy(** nazwa):
    suma = 0
    for cos in nazwa:
        suma += nazwa[cos]
    print(suma)
# zakupy(maka=4, woda=3, cukier=2, zapalniczka=1)


# zad.11
a = complex(3, 4)
b = complex(4, 3)
# czesci.rzeczywista(a)
# dodOdej.odejmij(a, b)
