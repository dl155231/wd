# zadanie 7 generatorem
def Foo(dane):
    for index in range(0, len(dane)):
        if index % 2 == 0:
            yield dane[index]


tekst = Foo("Konstantynopolitańczykowianeczka")
print(next(tekst))
print(next(tekst))
print(next(tekst))
print(next(tekst))
