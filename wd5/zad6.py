class Wspak:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


# string
wyraz = Wspak("Warszawa")
print(wyraz.__next__())
print(wyraz.__next__())
# lista
A = [1, 2, 3, 4, 5]
lista = Wspak(A)
print(lista.__next__())
print(lista.__next__())
# slownik
slownik = {
    "jeden": "1",
    "dwa": "2"
}
# # iterator nie działa dla słowników
# odwroc = Wspak(slownik)
# print(odwroc.__next__())
