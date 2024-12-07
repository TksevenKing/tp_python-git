import math 

# 2. Equation du second degree  ax2 + bx + c = 0
print("L'equation est souss cette forme ax2 + bx + c = 0")

a = float(input("saisir a: "))
b = float(input("saisir b: "))
c = float(input("saisir c: "))

def delta(a,b,c):
    delta = (b*b) - (4 * a * c)
    return delta

delta = delta(a,b,c)
print(f"delta= {delta}")

def nombreRacine(delta):
    if(delta > 0):
        return 2
    elif (delta == 0):
        return 1
    else:
        return 0
nbRacine = nombreRacine(delta)

def afficheNombreRacine(nbRacine):
    if(nbRacine == 2):
        print("2 solutions")
    elif (nbRacine == 1):
        print("1 solution")
    else: 
        print("pas de solution dans R car delta < 0")

afficheNombreRacine(nbRacine)

def racine1(a,b,c,delta):
    if(delta > 0 ):
        return (-b - math.sqrt(delta)) / (2*a)
    elif (delta == 0):
        return (-b)/(2*a)
def racine2(a,b,c,delta):
    return (-b + math.sqrt(delta)) / (2*a)

if(delta > 0):
    x1 = racine1(a,b,c,delta)
    x2 = racine2(a,b,c,delta)
    print(f"x1= {x1}, x2= {x2}")
elif (delta == 0):
    x = racine1(a,b,c,delta)
    print(f"x= {x}")
else:
    print("pas de solution dans R")

