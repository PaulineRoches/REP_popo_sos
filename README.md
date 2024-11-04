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

Le TP3 est réalisé dans le Jupyter Notebook `tp3.ipynb`. On trouve dedans les facteurs de variabilité, notre analyse des résultats et nos recommandations de valeurs pour les paramètres.

Le fichier `associativity.c.jinja` est le fichier contenant notre script testant l'associativité. A l'intérieur, nous avons identifié les facteurs que nous voulons faire varier avec nos tests en les passant en facteur en les mettant entre "{{ }}".

Le fichier `template.py` est le fichier où nous défnissons ce que notre script global doit faire : les différents facteurs à faire varier grâce au jinja et le traitement que l'on veut faire des sorties.

Le fichier `associativity-template.c` est le fichier résultant des changements appliqués par le template sur le jinja.

Les résultats sont stockés dans deux fichiers différents :
- `resultats_associativite_etendu.csv` : teste toutes les combinaisons de nos facteurs de variabilité
- `resultats_associativite.csv` : set représentatif du fichier resultats_associativite_etendu qui nous permet d'avoir des résultats pertinents afin de voir plus simplement les différences que les facteurs impliquent.