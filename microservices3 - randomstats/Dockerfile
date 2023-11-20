# Dockerfile pour le microservice de statistiques aléatoires
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "stats_service:app", "--host", "0.0.0.0", "--port", "8002"]
