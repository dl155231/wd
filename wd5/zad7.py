class Parzyste:

    def __init__(self, wyraz):
        self.wyraz = wyraz
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        index = self.index
        self.index += 2
        if (self.index > len(self.wyraz) + 1):
            raise StopIteration
        else:
            return self.wyraz[index]


wyraz = Parzyste("Złotówka")
print(next(wyraz))
print(next(wyraz))
