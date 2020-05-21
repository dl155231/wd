import pandas as pd
import matplotlib.pyplot as plt
import random as rd
import numpy as np

# # dodane jedynie w celach estetycznych
# # (wypośrodkowanie ticków)
def bins_labels(bins, **kwargs):
    bin_w = (max(bins) - min(bins)) / (len(bins) - 1)
    plt.xticks(np.arange(min(bins)+bin_w/2, max(bins), bin_w), bins, **kwargs)
    plt.xlim(bins[0], bins[-1])
# #

def rzucaj(x):
    rzut1 = [rd.randint(1, 6) for i in range(x)]
    rzut2 = [rd.randint(1, 6) for i in range(x)]
    suma = []
    for i in range(x):
        suma.append(rzut1[i]+rzut2[i])
    return suma


wynik = rzucaj(100000)
# # dodane jedynie w celach estetycznych
bins = range(1,14)
bins_labels(bins, fontsize=12)
# #
plt.hist(wynik, bins=bins, facecolor='g', alpha=0.75, density=False)
plt.xlabel('ilość oczek')
plt.ylabel('ilość trafień')
plt.show()
