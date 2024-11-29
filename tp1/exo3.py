# ce prog permet de calculer la vitesse 

# recuperer la distance et temps en minutes
d = float(input("saisir la distance en Km"))
t = float(input("Saisir le temps en minutes"))

# convertir la distance en metre  

distance = d * 1000
# convertir le temps en seconde
temps = t * 60

#calculer la vitesse v=d(m)/temps(s)
v = distance / temps

print(f"la vitesse est v= {v} m/s")
