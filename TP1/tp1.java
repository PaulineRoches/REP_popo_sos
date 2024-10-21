import java.util.Scanner;
import java.util.Random;

//Pour compiler : javac tp1.java
// Pour exécuter : java tp1

public class tp1 {
    public static double[] aleatoire() {
        // Générer trois chiffres aléatoires entre -100 et 100
        Random random = new Random();
        return new double[]{
            random.nextDouble() * 200 - 100, // entre -100 et 100
            random.nextDouble() * 200 - 100,
            random.nextDouble() * 200 - 100
        };
    }

    public static double[] chiffresUtilisateurs() {
        // Demander à l'utilisateur de saisir trois chiffres
        Scanner scanner = new Scanner(System.in);
        double[] chiffres = new double[3];

        System.out.print("Entrez le premier chiffre : ");
        chiffres[0] = scanner.nextDouble();
        System.out.print("Entrez le deuxième chiffre : ");
        chiffres[1] = scanner.nextDouble();
        System.out.print("Entrez le troisième chiffre : ");
        chiffres[2] = scanner.nextDouble();

        return chiffres;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int version = 0;

        // Boucle jusqu'à ce que l'utilisateur entre 1 ou 2
        while (version != 1 && version != 2) {
            System.out.print("Voulez-vous tester l'associativité en aléatoire (1) ou entrer vos propres nombres (2) ? ");
            version = scanner.nextInt();

            if (version != 1 && version != 2) {
                System.out.println("Option invalide, veuillez choisir 1 ou 2.");
            }
        }

        double x, y, z;
        if (version == 1) {
            double[] chiffres = aleatoire();
            x = chiffres[0];
            y = chiffres[1];
            z = chiffres[2];
            System.out.printf("Chiffres aléatoires générés : x=%.2f, y=%.2f, z=%.2f%n", x, y, z);
        } else {
            double[] chiffres = chiffresUtilisateurs();
            x = chiffres[0];
            y = chiffres[1];
            z = chiffres[2];
        }
        
        // Calculer les résultats
        double res1 = (x + y) + z;
        double res2 = x + (y + z);

        // Vérifier l'associativité
        if (res1 == res2) {
            System.out.printf("L'associativité est vérifiée : (x+y)+z == x+(y+z) = %.2f%n", res1);
        } else {
            System.out.printf("L'associativité n'est pas vérifiée : res1 = %.2f et res2 = %.2f%n", res1, res2);
        }

        // Fermer le scanner
        scanner.close();
    }
}