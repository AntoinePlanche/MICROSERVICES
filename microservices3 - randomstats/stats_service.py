from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/stats")
def read_random_stats():
    # Génération de quelques statistiques aléatoires
    data = {
        "random_number": random.randint(1, 100),
        "random_percentage": random.random(),
        "random_choice": random.choice(["Option A", "Option B", "Option C"])
    }
    return {"data": data}
