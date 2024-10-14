FROM gcc:latest

#Définir le répertoire de travail dans le conteneur
WORKDIR /app

COPY associativity.c /app/associativity.c
RUN apt-get update && apt-get install -y build-essential
RUN gcc -o app associativity.c

#Définir la commande par défaut qui sexécute lors du démarrage du conteneur
CMD ["./app"]
