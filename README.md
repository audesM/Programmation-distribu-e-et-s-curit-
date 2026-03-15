# Programmation-distribu-e-et-s-curit-
# - Objectif : Développer une application client-serveur en Python utilisant les sockets, où le serveur génère un nombre aléatoire, et le client doit le deviner.

## Partie 1 : Serveur
      Créer un programme serveur.py qui :
        - Crée un socket serveur TCP.
       - Accepte une connexion d’un client.
       - Génère un nombre secret aléatoire entre 1 et 100.
       - Attend les propositions du client.
       - Répond à chaque tentative avec :
          + "Trop petit" si le nombre proposé est inférieur au secret,
          + "Trop grand" si le nombre proposé est supérieur, 
          + "Bravo, vous avez trouvé !" si le client a deviné juste.
       - Termine la connexion lorsque le client a trouvé le bon nombre.
## Partie 2 : Client
         Créer un programme client.py qui :
            - Crée un socket client TCP.
            - Se connecte au serveur.
            - Affiche un message de bienvenue.
            - Envoie une proposition (saisie utilisateur) au serveur.
           - Affiche la réponse du serveur.
          - Continue jusqu’à ce que le serveur réponde "Bravo, vous avez trouvé !".
