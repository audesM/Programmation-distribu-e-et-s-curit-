import socket

HOST = '127.0.0.1' 
PORT = 65432

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
            
            #  Message de bienvenue
        print("--- Bienvenue dans le jeu du Nombre Secret ! ---")

            # Boucle de jeu
        while True:
            # Saisie utilisateur
            proposition = input("Proposez un nombre (entre 1 et 100) : ")
                
            # Envoi de la proposition au serveur (encodée en UTF-8)
            s.sendall(proposition.encode('utf-8'))

            # Réception de la réponse du serveur
            reponse = s.recv(1024).decode('utf-8')
            print(f"Réponse du serveur : {reponse}")

            #  Condition d'arrêt
            if "Bravo" in reponse:
                print("Fin de la partie. Merci d'avoir joué !")
                break
                    
except ConnectionRefusedError:
    print("Erreur : Le serveur n'est pas lancé ou l'adresse est incorrecte.")

