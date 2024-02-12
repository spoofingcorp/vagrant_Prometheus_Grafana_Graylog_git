import requests
import concurrent.futures
import matplotlib.pyplot as plt
from datetime import datetime

# Définir l'URL à tester
url = "http://192.168.33.11"

# Définir le nombre de requêtes à envoyer
num_requests = 1000

# Définir le nombre de threads à utiliser
num_threads = 10

# Créer une liste pour stocker les temps de réponse
response_times = []

# Créer une fonction pour envoyer une requête et mesurer le temps de réponse
def send_request(session):
    start_time = datetime.now()
    response = session.get(url)
    end_time = datetime.now()
    elapsed_time = (end_time - start_time).total_seconds()
    
    # Ajouter le temps de réponse à la liste
    response_times.append(elapsed_time)

    # Afficher le code de statut et la durée de la requête
    print(f"Status code: {response.status_code}, Time: {elapsed_time}")

# Créer une session pour réutiliser les connexions
session = requests.Session()

# Utiliser concurrent.futures pour gérer les threads de manière plus efficace
with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
    # Lancer les requêtes et mesurer le temps de réponse
    executor.map(lambda _: send_request(session), range(num_requests))

# Afficher un graphique en temps réel
plt.plot(response_times)
plt.title('Response Times Over Time')
plt.xlabel('Request Number')
plt.ylabel('Response Time (s)')
plt.show()

# Afficher un message de fin
print(f"Stress test completed. {num_requests} requests sent to {url}.")
