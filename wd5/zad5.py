class Osoba:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        return "{} {}".format(self.imie, self.nazwisko)


class Pracownik(Osoba):

    def __init__(self, imie, nazwisko, pensja):
        super().__init__(imie, nazwisko)
        self.pensja = pensja

    def przedstaw_sie(self):
        return "{} {} i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)


class Menadzer(Pracownik):

    def przedstaw_sie(self):
        return "{} {}, jestem menadżerem i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)


zdzichu = Pracownik("Zdzisław", "Bawaria", 2000)
tytus = Menadzer("Kapitan", "Bomba", 1337420)
print(isinstance(zdzichu, Pracownik))
print(isinstance(tytus, Pracownik))
print(issubclass(Pracownik, Osoba))
print(issubclass(Osoba, Pracownik))
print(issubclass(Menadzer, Pracownik))
print(issubclass(Osoba, Menadzer))
