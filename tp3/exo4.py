# import saisir_heure from exo3
from exo3 import *
# En usant la fct de l'exo3 saisr 2 haoraies et faire leur diff
print("Saisir horaire 1: ")
h1,m1,s1 = saisir_heure()
print("Saisir horaire 2: ")
h2,m2,s2 = saisir_heure()

horaire1 = conversion_temps(h1,m1,s1)
horaire2 = conversion_temps(h2,m2,s2)

print(f"le temps ecoule entre les deux horaires est: {horaire1 - horaire2}")
