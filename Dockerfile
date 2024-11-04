FROM gcc:latest

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier tous les fichiers nécessaires dans le conteneur
COPY . /app

# Installer Python, pip et créer un environnement virtuel
RUN apt-get update && \
    apt-get install -y python3 python3-venv && \
    python3 -m venv /app/venv && \
    /app/venv/bin/pip install --no-cache-dir jinja2

# Définir l’environnement virtuel dans le PATH
ENV PATH="/app/venv/bin:$PATH"

# Définir la commande par défaut
CMD ["python3", "template.py"]
