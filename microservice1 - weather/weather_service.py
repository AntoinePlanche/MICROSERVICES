from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/weather/{city}")
def read_weather(city: str):
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    # Inclure le champ timestamp dans la requête
    cursor.execute("SELECT id, temperature, description, timestamp FROM weather WHERE city = ?", (city,))
    data = cursor.fetchall()
    conn.close()
    # Structurer les données pour une meilleure lisibilité dans la réponse
    weather_data = [{
        'id': row[0],
        'temperature': row[1],
        'description': row[2],
        'timestamp': row[3]
    } for row in data]
    return {"data": weather_data}