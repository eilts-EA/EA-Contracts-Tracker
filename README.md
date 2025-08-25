# SDVOSB Contract Tracker (GitHub-ready)

This repo contains a FastAPI app with SAM.gov ingestion, Prometheus metrics, and Grafana dashboards.
See .env.example for configuration.

Quick start (local):
```bash
cp .env.example .env
docker compose up --build
```

App: http://localhost:8000
Grafana: http://localhost:3000 (admin/admin)
Prometheus: http://localhost:9090