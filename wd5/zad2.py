class Kwadrat:

    def __init__(self, x):
        self.x = x
        self.y = x

    def __add__(self, other):
        return self.x+other.x, self.y+other.y


kw1 = Kwadrat(5)
kw2 = Kwadrat(7)
kw3 = kw1 + kw2
print(kw3)
