# 1. ecrire une fonction qui retourne la somme des entiers de m a n (avec m<n) ::

def somme(m , n):
    temp = m
    while(temp < n):
        temp = temp +1
        m = m + temp
    print(f"somme= {m}")

somme(5,8)
