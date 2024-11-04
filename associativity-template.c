#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void aleatoire(double *x, double *y, double *z) {
    // Générer trois chiffres aléatoires entre -100 et 100
    *x = ((double)drand48()) * 5000 - 1000; 
    *y = ((double)drand48()) * 5000 - 1000;
    *z = ((double)drand48()) * 5000 - 1000;
}


void ecrireResultats(int totalExperiences, int associativiteVerifiee, double tauxAssociativite) {
     // Ouvrir le fichier CSV en mode écriture
    /*FILE *fichier = fopen("resultats_associativite.csv", "w");
    if (fichier == NULL) {
        perror("Erreur lors de l'ouverture du fichier");
        return;
    }

    // Écrire l'en-tête du fichier CSV
    fprintf(fichier, "Total des expériences,Associativité vérifiée,Taux d'associativité\n");

    // Écrire les données dans le fichier
    fprintf(fichier, "%d,%d,%.2f\n", totalExperiences, associativiteVerifiee, tauxAssociativite);

    // Fermer le fichier
    fclose(fichier);*/

    // Afficher le taux d'associativité dans la console pour vérification
    printf("%.2f\n", tauxAssociativite);
}

void calculerTauxAssociativite(int totalExperiences) {
    double x, y, z;
    int associativiteVerifiee = 0;

    // Exécuter lexpérience un certain nombre de fois
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
    srand48(time(NULL));

    int totalExperiences=50000;

    calculerTauxAssociativite(80000);
    
    return 0;
}