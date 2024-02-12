import tkinter as tk
from tkinter import ttk
import threading
import requests

class StressTestApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Test de Stress HTTP")

        # Éléments de l'interface
        self.create_widgets()

    def create_widgets(self):
        # URL
        self.url_label = ttk.Label(self, text="URL:")
        self.url_label.grid(column=0, row=0)
        self.url_entry = ttk.Entry(self)
        self.url_entry.grid(column=1, row=0)

        # Nombre de threads
        self.thread_label = ttk.Label(self, text="Nombre de Threads:")
        self.thread_label.grid(column=0, row=1)
        self.thread_spinbox = ttk.Spinbox(self, from_=1, to=100)
        self.thread_spinbox.grid(column=1, row=1)

        # Nombre d'itérations
        self.iter_label = ttk.Label(self, text="Nombre d'Itérations:")
        self.iter_label.grid(column=0, row=2)
        self.iter_spinbox = ttk.Spinbox(self, from_=1, to=1000)
        self.iter_spinbox.grid(column=1, row=2)

        # Bouton de démarrage
        self.start_button = ttk.Button(self, text="Démarrer le Test", command=self.start_test)
        self.start_button.grid(column=1, row=3)

        # Zone de texte pour les logs
        self.log_text = tk.Text(self, height=10, width=50)
        self.log_text.grid(column=0, row=4, columnspan=2)

    def log_message(self, message):
        self.log_text.insert(tk.END, message + '\n')
        self.log_text.see(tk.END)

    def send_requests(self, url, iterations):
        for _ in range(iterations):
            try:
                response = requests.get(url)
                self.log_message(f"Réponse: {response.status_code}")
            except requests.exceptions.RequestException as e:
                self.log_message(f"Erreur: {e}")

    def start_test(self):
        url = self.url_entry.get()
        num_threads = int(self.thread_spinbox.get())
        iterations = int(self.iter_spinbox.get())

        for _ in range(num_threads):
            thread = threading.Thread(target=self.send_requests, args=(url, iterations))
            thread.start()

if __name__ == "__main__":
    app = StressTestApp()
    app.mainloop()
