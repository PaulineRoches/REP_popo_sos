from jinja2 import Template
import subprocess

template_content = open('associativity.c.jinja').read()
template=Template(template_content)

factors = {
    "random_choice": "rand() / RAND_MAX" 
}

generated_code = template.render(factors)

with open("associativity-template.c", "w") as f:
    f.write(generated_code)

compile_process = subprocess.run(['gcc', '-o', 'associativity_app', 'associativity-template.c'], capture_output=True, text=True)
run_process = subprocess.run(['./associativity_app'], capture_output=True, text=True)
print(run_process.stdout)