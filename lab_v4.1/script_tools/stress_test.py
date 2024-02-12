# Importer les modules nécessaires
import requests
import time
import threading

# Définir l'URL à tester
url = "http://192.168.33.11"

# Définir le nombre de requêtes à envoyer
num_requests = 10

# Créer une fonction pour envoyer une requête
def send_request():
    # Envoyer une requête GET à l'URL
    response = requests.get(url)
    # Afficher le code de statut et la durée de la requête
    print(f"Status code: {response.status_code}, Time: {response.elapsed.total_seconds()}")

# Créer une liste pour stocker les threads
threads = []

# Créer une boucle pour créer et démarrer les threads
for i in range(num_requests):
    # Créer un thread qui exécute la fonction send_request
    thread = threading.Thread(target=send_request)
    # Ajouter le thread à la liste
    threads.append(thread)
    # Démarrer le thread
    thread.start()

# Créer une boucle pour attendre que tous les threads se terminent
for thread in threads:
    # Attendre que le thread se termine
    thread.join()

# Afficher un message de fin
print(f"Stress test completed. {num_requests} requests sent to {url}.")
