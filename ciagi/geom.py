# ciągi geometryczne


def suma(a1, q, n):
    if q == 1:
        return a1*n
    else:
        return a1*(1-q**n)/1-q


def nty(a1, q, n):
    return a1*(q**(n-1))
