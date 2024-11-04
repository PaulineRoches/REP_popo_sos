import csv
from jinja2 import Template
import subprocess

template_content = open('associativity.c.jinja').read()
template=Template(template_content)

factor_combinations = [
    {
        "random_choice": "rand() / RAND_MAX" ,
        "type_choice" : "double",
        "max_choice": "2000",
        "min_choice":"0",
        "num_exp":"50000"
    },
    {
        "random_choice": "rand() / RAND_MAX" ,
        "type_choice" : "double",
        "max_choice": "200",
        "min_choice":"100",
        "num_exp":"50000"
    },
    {
        "random_choice": "rand() / RAND_MAX" ,
        "type_choice" : "float",
        "max_choice": "200",
        "min_choice":"100",
        "num_exp":"50000"
    },
    {
        "random_choice": "rand() / RAND_MAX" ,
        "type_choice" : "int",
        "max_choice": "200",
        "min_choice":"100",
        "num_exp":"50000"
    },
    {
        "random_choice": "drand48()" ,
        "type_choice" : "double",
        "max_choice": "200",
        "min_choice":"100",
        "num_exp":"50000"
    },
    {
        "random_choice": "rand() / RAND_MAX" ,
        "type_choice" : "double",
        "max_choice": "200",
        "min_choice":"100",
        "num_exp":"100"
    },
    {
        "random_choice": "rand() / RAND_MAX" ,
        "type_choice" : "double",
        "max_choice": "2000",
        "min_choice":"0",
        "num_exp":"100"
    },   
    {
        "random_choice": "rand() / RAND_MAX" ,
        "type_choice" : "double",
        "max_choice": "50",
        "min_choice":"-50",
        "num_exp":"3000"
    }, 
    {
        "random_choice": "rand() / RAND_MAX" ,
        "type_choice" : "double",
        "max_choice": "2000",
        "min_choice":"0",
        "num_exp":"3"
    },
    {
        "random_choice": "rand() / RAND_MAX" ,
        "type_choice" : "double",
        "max_choice": "800000",
        "min_choice":"-800000",
        "num_exp":"80000"
    },
    {
        "random_choice": "rand() / RAND_MAX" ,
        "type_choice" : "double",
        "max_choice": "5000",
        "min_choice":"-20",
        "num_exp":"600"
    },
    {
        "random_choice": "rand() / RAND_MAX" ,
        "type_choice" : "double",
        "max_choice": "5000",
        "min_choice":"1000",
        "num_exp":"80000"
    }
]

#factors = {
#    "random_choice": "rand() / RAND_MAX" ,
#    "type_choice" : "double",
#    "max_choice": "2000",
#    "min_choice":"0",
#    "num_exp":"50000"
#}
with open("resultats_associativite.csv", mode="w", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)
    # Écrire l'en-tête
    csv_writer.writerow([
        "RandomChoice", "TypeChoice", "MaxChoice", "MinChoice", "NumExp", "TotalExperiences", "TauxAssociativite"
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
            factors["num_exp"],  # Peut être modifié pour `totalExperiences` si nécessaire
            taux_associativite
        ])


