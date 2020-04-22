class Material:
    def __init__(self, rodzaj, długosc, szerokosc):
        self.rodzaj = rodzaj
        self.dlugosc = długosc
        self.szerokosc = szerokosc

    def wyswietl_nazwe(self):
        return self.rodzaj + " " + self.dlugosc + " " + self.szerokosc


class Ubrania(Material):
    def __init__(self, rozmiar, kolor, dla_kogo):
        self.rozmiar = rozmiar
        self.kolor = kolor
        self.dla_kogo = dla_kogo

    def wyswietl_dane(self):
        return self.rozmiar + " " + self.kolor + " " + self.dla_kogo


class Sweter(Ubrania):
    def __init__(self, rodzaj_swetra):
        self.rodzaj_swetra = rodzaj_swetra

    def wyswietl_dane(self):
        return self.rodzaj_swetra


Bawełna = Material("poliester", "1", "1")
print(Bawełna.wyswietl_nazwe())
Bluza = Ubrania("M", "biały", "damska")
print(Bluza.wyswietl_dane())
Sw = Sweter("kardigan")
print(Sw.wyswietl_dane())
