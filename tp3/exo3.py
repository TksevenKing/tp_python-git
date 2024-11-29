#Convertit le temps donner en hh:mm:ss en seconde exemple : 1h 15 min 10 s donne 4510 s
def saisir_heure():
    h = int(input("saisir heure: "))
    m = int(input("saisir minute: "))
    s = int(input("saisir seconde: "))
    return h,m,s

h,m,s = saisir_heure()

def conversion_temps(h,m,s):
    temps = (h*3600) + (m*60) + s
    return temps

temps = conversion_temps(h,m,s)
print(f"le temps en seconde est : {temps}")