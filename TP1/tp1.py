#pour lancer : python3 tp1.py

import random

def aleatoire():
    #Générer trois chiffres aléatoires.
    return random.uniform(-100, 100), random.uniform(-100, 100), random.uniform(-100, 100)

def chiffresUtilisateurs():
    #Demander à l'utilisateur de saisir trois chiffres.
    x = float(input("Entrez le premier chiffre : "))
    y = float(input("Entrez le deuxième chiffre : "))
    z = float(input("Entrez le troisième chiffre : "))
    return x, y, z

def main():

    version=0
     
    while version not in [1, 2]:
        version = int(input("Voulez-vous tester l'associativité en aléatoire (1) ou entrer vos propres nombres (2) ? "))

        if version not in [1, 2]:
            print("Option invalide, veuillez choisir 1 ou 2.")

    if version == 1:
        x, y, z = aleatoire()
        print(f"Chiffres aléatoires générés : x={x}, y={y}, z={z}")
    elif version == 2:
        x, y, z = chiffresUtilisateurs()

    # Calculer les résultats
    res1 = (x + y) + z
    res2 = x + (y + z)

    # Vérifier l'associativité
    if res1 == res2:
        print(f"L'associativité est vérifiée : (x+y)+z == x+(y+z) = {res1}")
    else:
        print(f"L'associativité n'est pas vérifiée : res1 = {res1} et res2 = {res2}")

if __name__ == "__main__":
    main()
