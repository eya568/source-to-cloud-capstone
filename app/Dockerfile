FROM python:3.12-slim

WORKDIR /app

# curl est nécessaire ici : le healthcheck défini dans docker-compose.yml
# s'exécute À L'INTÉRIEUR du conteneur, il a donc besoin de son propre curl.
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN adduser --disabled-password --gecos '' appuser && \
    chown -R appuser:appuser /app
USER appuser

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "-w", "2", "app:app"]
