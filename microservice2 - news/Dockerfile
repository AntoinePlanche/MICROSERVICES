# Dockerfile pour le microservice de données actualités
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "news_service:app", "--host", "0.0.0.0", "--port", "8001"]
