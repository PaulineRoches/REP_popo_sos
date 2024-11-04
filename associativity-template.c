#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void aleatoire(int *x, int *y, int *z) {
    // Générer trois chiffres aléatoires entre -100 et 100
    *x = ((int)rand() / RAND_MAX) * 50 - 100; 
    *y = ((int)rand() / RAND_MAX) * 50 - 100;
    *z = ((int)rand() / RAND_MAX) * 50 - 100;
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
    int x, y, z;
    int associativiteVerifiee = 0;

    // Exécuter lexpérience un certain nombre de fois
    for (int i = 0; i < totalExperiences; i++) {
        aleatoire(&x, &y, &z);

        // Calculer les résultats
        int res1 = (x + y) + z;
        int res2 = x + (y + z);

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
    int x, y, z;
    int version = 0;

    // Initialiser le générateur de nombres aléatoires
    (time(NULL));

    int totalExperiences=50000;

    calculerTauxAssociativite(50000);
    
    return 0;
}