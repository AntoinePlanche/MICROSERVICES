# Dockerfile pour le microservice de données climatiques
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier des dépendances et installer les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier les fichiers source du microservice dans le conteneur
COPY . .

# Commande pour lancer l'application
CMD ["uvicorn", "weather_service:app", "--host", "0.0.0.0", "--port", "8000"]