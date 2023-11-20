import sqlite3
import sqlite3
from datetime import datetime, timedelta
import random

# Connexion à SQLite
conn = sqlite3.connect('weather_data.db')

# Création d'une table avec un timestamp
conn.execute('''
CREATE TABLE IF NOT EXISTS weather (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    city TEXT NOT NULL,
    temperature REAL NOT NULL,
    description TEXT NOT NULL,
    timestamp DATETIME NOT NULL
)
''')

# Fonction pour générer des données fictives avec des timestamps
def generate_weather_data(city, num_entries):
    descriptions = ["Sunny", "Cloudy", "Rain", "Snow", "Fog"]
    for _ in range(num_entries):
        temperature = random.uniform(-10, 30)  # Température aléatoire entre -10 et 30
        description = random.choice(descriptions)
        timestamp = datetime.now() - timedelta(days=random.randint(0, 30))  # Timestamp aléatoire dans les 30 derniers jours
        conn.execute("INSERT INTO weather (city, temperature, description, timestamp) VALUES (?, ?, ?, ?)",
                     (city, temperature, description, timestamp))

# Générer et insérer des données fictives
generate_weather_data("Montreal", 200)

# Sauvegarde des changements et fermeture de la connexion
conn.commit()
conn.close()