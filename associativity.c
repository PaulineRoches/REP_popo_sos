#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void aleatoire(double *x, double *y, double *z) {
    // Générer trois chiffres aléatoires entre -100 et 100
    *x = ((double)rand() / RAND_MAX) * 200 - 100; 
    *y = ((double)rand() / RAND_MAX) * 200 - 100;
    *z = ((double)rand() / RAND_MAX) * 200 - 100;
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

    int totalExperiences=50000;

    calculerTauxAssociativite(totalExperiences);
    
    return 0;
}