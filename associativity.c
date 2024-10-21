#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void aleatoire(double *x, double *y, double *z) {
    // Générer trois chiffres aléatoires entre -100 et 100
    *x = ((double)rand() / RAND_MAX) * 200 - 100; 
    *y = ((double)rand() / RAND_MAX) * 200 - 100;
    *z = ((double)rand() / RAND_MAX) * 200 - 100;
}


void ecrireResultats(int totalExperiences, int associativiteVerifiee, double tauxAssociativite) {
    /*FILE *fichier = fopen("answer_associativity.txt", "w");
    if (fichier == NULL) {
        perror("Erreur lors de l'ouverture du fichier");
        return;
    }*/

    //fprintf(fichier, "Sur %d expériences, l'associativité a été vérifiée %d fois.\n", totalExperiences, associativiteVerifiee);
    //fprintf(fichier, "Le taux d'associativité est de %.2f%%.\n", tauxAssociativite);
    //fprintf(fichier, "%.2f", tauxAssociativite);
    //fclose(fichier);
    printf("%.2f\n", tauxAssociativite);
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

    ecrireResultats(totalExperiences, associativiteVerifiee, tauxAssociativite);
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