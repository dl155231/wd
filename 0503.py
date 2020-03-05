import sys
'''
# # # cw02

# # zad01
zdanie = "Litwo! Ojczyzno moja!"
print(zdanie.count(" "))

# # zad02
a = sys.stdin.readline()
b = sys.stdin.readline()
wynik = int(a)*int(b)
sys.stdout.write(str(wynik)+"\n")


# # zad03
# ==
# !=
# <
# <=
# >
# >=

# # zad04
liczba = input("Podaj liczbe: ")
liczba = int(liczba)
if liczba < 0:
    print(-liczba)
else:
    print(liczba)

# # zad05
a = input("Podaj liczbe a: ")
b = input("Podaj liczbe b: ")
c = input("Podaj liczbe c: ")
a = int(a)
b = int(b)
c = int(c)
if ((int(a) in range(1,11)) and (a>b or b>c)):
    print("Spełnia")
else:
    print("Nie spełnia")

# # zad06
for x in range(101):
    if not (x%5):
        print(x)
'''

# # zad08

'''
# # zad09
x = input("Podaj liczbe wielocyfrowa: ")
x = int(x)
suma = 0
while (x>0):
    suma += int(x%10)
    x=x/10
print(suma)

# # zad10
n=input("Podaj wysokosc wiezy: ")
n=int(n)
for i in range(n+1):
    for j in range(i):
        sys.stdout.write("A")
    print()

# # zad11


# # zad12
for x in range(1,11):
    for y in range(1,11):
        print(str(x)+ "*" + str(y) + " = " + str(x*y)+ "\n")
'''

# # zad15
x='a'
def sqRoot(x):
    try:
        result = x*x
    except TypeError:
       result = "Please enter a number"
    return result
sqRoot(x)