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

for factors in factor_combinations:
    generated_code = template.render(factors)
    with open("associativity-template.c", "w") as f:
        f.write(generated_code)

    compile_process = subprocess.run(['gcc', '-o', 'associativity_app', 'associativity-template.c'], capture_output=True, text=True)
    run_process = subprocess.run(['./associativity_app'], capture_output=True, text=True)
    print(f"Running check for factors :  {factors}")
    print(run_process.stdout)