# REP_Popo_Soso

## TP1 

Les différents codes pour tester l'associativité sont dans le dossier `TP1` : on y trouve le même programmes en Python, en Java et en C.

## TP2

Nous avons gardé le programme en C en ne gardant que l'essentiel dans le fichier `associativity.c`.

Pour lancer le programme, dans un terminal : 
 - compiler le code : gcc associativity.c -o associativity
 - exécuter le code : ./associativity

Le code réalise le test d'associativité pour 50 000 expériences avec x, y et z aléatoires. Puis, le taux d'associativité est affiché dans `answer_associativity.txt`.
Vous devriez obtenir un taux d'associativité d'environ 92%.

Nous avons mis en place un GitHub Actions avec le `Dockerfile` : il teste le programme et stocke le résultat dans `answer_associativity.txt`.

## TP3

Pour le TP3, il faut se placer dans la branche `template`.
