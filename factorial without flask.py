try:
    x=int(input("Entrez un nombre:"))
    F=1
    for i in range(1,x+1):
        F=F*i
    print(f"le factoriel de {x} est : {F}")
except ValueError as e:
    print(f"Erreur :{e}")