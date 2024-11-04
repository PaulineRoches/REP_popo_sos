FROM gcc:latest

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier tous les fichiers nécessaires dans le conteneur
COPY . /app

# Installer Python et les dépendances nécessaires pour Jinja2
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip3 install jinja2

# Installer build-essential (si d'autres outils sont nécessaires pour gcc)
RUN apt-get install -y build-essential

# Commande pour exécuter template.py qui lance les tests et génère les résultats
CMD ["python3", "template.py"]
