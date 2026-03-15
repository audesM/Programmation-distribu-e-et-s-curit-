import socket
import random

    # Configuration de l'adresse et du port
HOST = '127.0.0.1'  
PORT = 65432        

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Le serveur est prêt et écoute sur {HOST}:{PORT}...")

        # Accepter la connexion d'un client
    conn, addr = s.accept()
    with conn:
        print(f"Connecté par {addr}")

            # Générer le nombre secret (entre 1 et 100)
        nombre_secret = random.randint(1, 100)
        print(f"Nombre secret généré : {nombre_secret}")

            # Boucle d'attente des propositions du client
        while True:
            donnees = conn.recv(1024).decode('utf-8')
            if not donnees:
                break
                
            try:
                proposition = int(donnees)
            except ValueError:
                conn.sendall("Veuillez envoyer un nombre valide.".encode('utf-8'))
                continue

                # Logique de comparaison
            if proposition < nombre_secret:
                reponse = "Trop petit"
            elif proposition > nombre_secret:
                reponse = "Trop grand"
            else:
                reponse = "Bravo, vous avez trouvé !"
                conn.sendall(reponse.encode('utf-8'))
                break # On sort de la boucle pour fermer la connexion
                
            conn.sendall(reponse.encode('utf-8'))

print("Connexion terminée.")

