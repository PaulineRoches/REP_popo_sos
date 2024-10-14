#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void aleatoire(double *x, double *y, double *z) {
    // Générer trois chiffres aléatoires entre -100 et 100
    *x = ((double)rand() / RAND_MAX) * 200 - 100; 
    *y = ((double)rand() / RAND_MAX) * 200 - 100;
    *z = ((double)rand() / RAND_MAX) * 200 - 100;
}

void chiffresUtilisateurs(double *x, double *y, double *z) {
    // Demander à l'utilisateur de saisir trois chiffres
    printf("Entrez le premier chiffre : ");
    scanf("%lf", x);
    printf("Entrez le deuxième chiffre : ");
    scanf("%lf", y);
    printf("Entrez le troisième chiffre : ");
    scanf("%lf", z);
}

void calculerTauxAssociativite(int totalExperiences) {
    double x, y, z;
    int associativiteVerifiee = 0;

    // Exécuter l'expérience un certain nombre de fois
    for (int i = 0; i < totalExperiences; i++) {
        aleatoire(&x, &y, &z);

        // Calculer les résultats
        double res1 = (x + y) + z;
        double res2 = x + (y + z);

        // Vérifier l'associativité
        if (res1 == res2) {
            associativiteVerifiee++;
        }
    }

    // Calculer le taux d'associativité
    double tauxAssociativite = (double)associativiteVerifiee / totalExperiences * 100;

    printf("Sur %d expériences, l'associativité a été vérifiée %d fois.\n", totalExperiences, associativiteVerifiee);
    printf("Le taux d'associativité est de %.2f%%.\n", tauxAssociativite);
}

int main() {
    double x, y, z;
    int version = 0;

    // Initialiser le générateur de nombres aléatoires
    srand(time(NULL));

    // Boucle jusqu'à ce que l'utilisateur entre 1 ou 2
    while (version != 1 && version != 2 && version!=3 ) {
        printf("Voulez-vous tester l'associativité en aléatoire (1), entrer vos propres nombres (2) ou calculer un taux d'associativité (3) ? ");
        scanf("%d", &version);

        if (version != 1 && version != 2 && version != 3) {
            printf("Option invalide, veuillez choisir 1, 2 ou 3.\n");
        }
    }
  
    if (version == 1) {
        aleatoire(&x, &y, &z);
        printf("Chiffres aléatoires générés : x=%.2f, y=%.2f, z=%.2f\n", x, y, z);
    } else if (version == 2) {
        chiffresUtilisateurs(&x, &y, &z);
    } else if (version == 3) {
        int totalExperiences;

        printf("Combien de fois voulez-vous exécuter l'expérience ? ");
        scanf("%d", &totalExperiences);
        
        // Assurez-vous que le nombre d'expériences est positif
        if (totalExperiences > 0) {
            calculerTauxAssociativite(totalExperiences);
        } else {
            printf("Le nombre d'expériences doit être positif.\n");
        }
    }

    // Calculer les résultats pour les options 1 et 2
    if (version == 1 || version == 2) {
        double res1 = (x + y) + z;
        double res2 = x + (y + z);

        // Vérifier l'associativité
        if (res1 == res2) {
            printf("L'associativité est vérifiée : (x+y)+z == x+(y+z) = %.2f\n", res1);
        } else {
            printf("L'associativité n'est pas vérifiée : res1 = %.2f et res2 = %.2f\n", res1, res2);
        }
    }

    return 0;
}