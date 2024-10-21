FROM ubuntu:20.04

#Définir le répertoire de travail dans le conteneur
WORKDIR /app

COPY associativity.c /app/associativity.c
RUN apt-get update && apt-get install -y build-essential clang
RUN clang -o app associativity.c

#Définir la commande par défaut qui sexécute lors du démarrage du conteneur
CMD ["./app"]
