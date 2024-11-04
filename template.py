import csv
import itertools
from jinja2 import Template
import subprocess

template_content = open('associativity.c.jinja').read()
template=Template(template_content)

#factors = {
#    "random_choice": "rand() / RAND_MAX" ,
#    "type_choice" : "double",
#    "max_choice": "2000",
#    "min_choice":"0",
#    "num_exp":"50000"
#}
factor_combinations = [
    {
        "random_choice": "rand() / RAND_MAX" ,
        "type_choice" : "double",
        "max_choice": "2000",
        "min_choice":"0",
        "num_exp":"50000",
        "fonction_initialisation":"srand"
    },
    {
        "random_choice": "rand() / RAND_MAX" ,
        "type_choice" : "double",
        "max_choice": "200",
        "min_choice":"100",
        "num_exp":"50000",
        "fonction_initialisation":"srand"
    },
    {
        "random_choice": "rand() / RAND_MAX" ,
        "type_choice" : "float",
        "max_choice": "200",
        "min_choice":"100",
        "num_exp":"50000",
        "fonction_initialisation":"srand"
    },
    {
        "random_choice": "rand() / RAND_MAX" ,
        "type_choice" : "int",
        "max_choice": "200",
        "min_choice":"100",
        "num_exp":"50000",
        "fonction_initialisation":"srand"
    },
    {
        "random_choice": "rand() / RAND_MAX" ,
        "type_choice" : "int",
        "max_choice": "700",
        "min_choice":"0",
        "num_exp":"6325059",
        "fonction_initialisation":"srand"
    },
    {
        "random_choice": "rand() / RAND_MAX" ,
        "type_choice" : "int",
        "max_choice": "80000",
        "min_choice":"-80000",
        "num_exp":"6000",
        "fonction_initialisation":"srand"
    },
    {
        "random_choice": "rand() / RAND_MAX" ,
        "type_choice" : "int",
        "max_choice": "200",
        "min_choice":"100",
        "num_exp":"100",
        "fonction_initialisation":"srand"
    },
    {
        "random_choice": "drand48()" ,
        "type_choice" : "double",
        "max_choice": "200",
        "min_choice":"100",
        "num_exp":"50000"
    },
    {
        "random_choice": "drand48()" ,
        "type_choice" : "double",
        "max_choice": "7000",
        "min_choice":"-7000",
        "num_exp":"8000",
        "fonction_initialisation":"srand48"
    },
    {
        "random_choice": "drand48()" ,
        "type_choice" : "double",
        "max_choice": "9000",
        "min_choice":"100",
        "num_exp":"80",
        "fonction_initialisation":"srand48"
    },
    {
        "random_choice": "drand48()" ,
        "type_choice" : "double",
        "max_choice": "150",
        "min_choice":"125",
        "num_exp":"8401684",
        "fonction_initialisation":"srand48"
    },
    {
        "random_choice": "rand() / RAND_MAX" ,
        "type_choice" : "double",
        "max_choice": "200",
        "min_choice":"100",
        "num_exp":"100",
        "fonction_initialisation":"srand"
    },
    {
        "random_choice": "rand() / RAND_MAX" ,
        "type_choice" : "double",
        "max_choice": "2000",
        "min_choice":"0",
        "num_exp":"100",
        "fonction_initialisation":"srand"
    },   
    {
        "random_choice": "rand() / RAND_MAX" ,
        "type_choice" : "double",
        "max_choice": "50",
        "min_choice":"-50",
        "num_exp":"3000",
        "fonction_initialisation":"srand"
    }, 
    {
        "random_choice": "rand() / RAND_MAX" ,
        "type_choice" : "double",
        "max_choice": "2000",
        "min_choice":"0",
        "num_exp":"3",
        "fonction_initialisation":"srand"
    },
    {
        "random_choice": "rand() / RAND_MAX" ,
        "type_choice" : "double",
        "max_choice": "800000",
        "min_choice":"-800000",
        "num_exp":"80000",
        "fonction_initialisation":"srand"
    },
    {
        "random_choice": "rand() / RAND_MAX" ,
        "type_choice" : "double",
        "max_choice": "5000",
        "min_choice":"-20",
        "num_exp":"600",
        "fonction_initialisation":"srand"
    },
    {
        "random_choice": "rand() / RAND_MAX" ,
        "type_choice" : "double",
        "max_choice": "5000",
        "min_choice":"1000",
        "num_exp":"80000",
        "fonction_initialisation":"srand"
    },
    {
        "random_choice": "drand48()" ,
        "type_choice" : "double",
        "max_choice": "5000",
        "min_choice":"1000",
        "num_exp":"80000",
        "fonction_initialisation":"srand48"
    }
]

## POUR CSV ETENDU

# Définitions des valeurs possibles pour chaque facteur
random_choices = ["rand() / RAND_MAX", "drand48()"]
type_choices = ["double", "float", "int"]
max_choices = ["2000", "200", "50", "800000", "5000"]
min_choices = ["0", "100", "-50", "-800000", "-20", "1000"]
num_exp_choices = ["50000", "100", "3000", "3", "80000", "600"]

# Définir la valeur de fonction_d_initialisation pour chaque choix de random_choice
fonction_d_initialisation_map = {
    "rand() / RAND_MAX": "srand(time(NULL));",  # Initialisation pour rand()
    "drand48()": "srand48(time(NULL));"         # Initialisation pour drand48()
}

# Générer toutes les combinaisons possibles de facteurs
extended_factor_combinations = list(itertools.product(random_choices, type_choices, max_choices, min_choices, num_exp_choices))



with open("resultats_associativite.csv", mode="w", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)
    # Écrire l'en-tête
    csv_writer.writerow([
        "RandomChoice", "TypeChoice", "MaxChoice", "MinChoice", "NumExp", "TauxAssociativite"
    ])

    for factors in factor_combinations:
        generated_code = template.render(factors)
        with open("associativity-template.c", "w") as f:
            f.write(generated_code)

        compile_process = subprocess.run(['gcc', '-o', 'associativity_app', 'associativity-template.c'], capture_output=True, text=True)
        run_process = subprocess.run(['./associativity_app'], capture_output=True, text=True)
        print(f"Running check for factors :  {factors}")
        print(run_process.stdout)
        # Ouvrir le fichier CSV pour écrire les résultats

        try:
            taux_associativite = float(run_process.stdout.strip())
        except ValueError:
            print("Erreur dans la conversion du résultat:", run_process.stdout)
            continue

        # Écrire les facteurs et le résultat dans le fichier CSV
        csv_writer.writerow([
            factors["random_choice"], 
            factors["type_choice"], 
            factors["max_choice"], 
            factors["min_choice"], 
            factors["num_exp"],
            taux_associativite
        ])

with open("resultats_associativite_etendu.csv", mode="w", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow([
        "RandomChoice", "TypeChoice", "MaxChoice", "MinChoice", "TotalExperiences", "TauxAssociativite"
    ])

    for factors in extended_factor_combinations:
        # Générer le dictionnaire de facteurs
        factors_dict = {
            "random_choice": factors[0],
            "type_choice": factors[1],
            "max_choice": factors[2],
            "min_choice": factors[3],
            "num_exp": factors[4],
            "fonction_d_initialisation": fonction_d_initialisation_map[factors[0]]
        }

        # Générer et écrire le code C
        generated_code = template.render(**factors_dict)
        with open("associativity-template.c", "w") as f:
            f.write(generated_code)

        # Compiler et exécuter le code
        compile_process = subprocess.run(['gcc', '-o', 'associativity_app', 'associativity-template.c'], capture_output=True, text=True)
        if compile_process.returncode != 0:
            print(f"Erreur de compilation pour les facteurs : {factors_dict}")
            print(compile_process.stderr)
            continue

        run_process = subprocess.run(['./associativity_app'], capture_output=True, text=True)
        try:
            taux_associativite = float(run_process.stdout.strip())
        except ValueError:
            print("Erreur dans la conversion du résultat:", run_process.stdout)
            continue

        # Écriture dans le CSV étendu
        csv_writer.writerow([
            factors_dict["random_choice"], 
            factors_dict["type_choice"], 
            factors_dict["max_choice"], 
            factors_dict["min_choice"], 
            factors_dict["num_exp"],
            taux_associativite
        ])

