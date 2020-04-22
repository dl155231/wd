class Sam:

    def __init__(self, wyraz):
        self.wyraz = wyraz
        self.samogloski = "aeyuioóąę"
        self.pozycja = 0

    def zwroc_wyraz(self):
        return self.wyraz

    def __iter__(self):
        return self

    def __next__(self):
        if isinstance(self.wyraz, str):
            if len(self.wyraz) == 0:
                raise StopIteration
            else:
                while True:
                    pozycja = self.pozycja
                    self.pozycja += 1
                    if self.wyraz[pozycja] in self.samogloski and self.pozycja < len(self.wyraz):
                        return self.wyraz[pozycja]
                    elif self.pozycja == len(self.wyraz):
                        raise StopIteration
        else:
            return "To nie jest string!"


wyraz = Sam("Zażółć gęślą jaźń")
print(next(wyraz))
print(next(wyraz))
print(next(wyraz))
