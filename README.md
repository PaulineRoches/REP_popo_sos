# REP_Popo_Soso

## TP1 

Les différents codes pour tester l'associativité sont dans le dossier `TP1` : on y trouve le même programmes en Python, en Java et en C.

## TP2

Nous avons gardé le programme en C en ne gardant que l'essentiel dans le fichier `associativity.c`.

Pour lancer le programme, dans un terminal : 
 - compiler le code : gcc tp1.c -o tp1
 - exécuter le code : ./tp1

Trois options s'offrent à vous : 
 - Pour lancer le mode aléatoire et le calcul du taux, choisir 3
 - Pour lancer le test d'associativité avec vos propres nombres, choisir 2
 - Pour lancer le test d'associativité avec des nombres aléatoires, choisir 1

Afin de réaliser l'expérience, lancer 3 et choisir le nombre d'expériences à réaliser : 50 000.
Vous devriez obtenir un taux d'associativité d'environ 92%.

Nous avons mis en place un GitHub Actions avec le `Dockerfile` : il teste le programme et stocke le résultat dans `answer_associativity.txt`.

## TP3

Le TP3 est réalisé dans le Jupyter Notebook `tp3.ipynb`.