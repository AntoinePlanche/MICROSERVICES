from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
from datetime import datetime, timedelta
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY = '253edf8e491849149785245325d78502'  # Remplacez par votre clé API de NewsAPI

@app.get("/news")
def read_news():
    # Définir une période pour les nouvelles, par exemple les dernières 24 heures
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)
    
    # Construire l'URL pour obtenir des nouvelles dans cette période
    url = f"https://newsapi.org/v2/everything?q=breaking-news&from={start_date.isoformat()}&to={end_date.isoformat()}&sortBy=publishedAt&apiKey={API_KEY}"

    response = requests.get(url)
    data = response.json()
    
    # Sélection aléatoire d'un article parmi les résultats
    articles = data.get("articles", [])
    if articles:
        random_article = random.choice(articles)
        return {"article": random_article}
    else:
        return {"message": "No new articles found in the last 24 hours."}
