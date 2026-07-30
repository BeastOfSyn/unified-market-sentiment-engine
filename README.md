# InsightBridge - Unified Market Sentiment Engine

InsightBridge is a full-stack Business Intelligence pipeline integrating an e-commerce customer feedback portal with external market trends (such as Reddit feed sentiment analysis).

## Architecture

This project is built using:
- **Backend**: Python 3.11, FastAPI, SQLAlchemy 2.0 (asyncpg), Alembic, Pydantic v2
- **Frontend**: React, Vite, Tailwind CSS, TanStack Query (React Query) v5
- **Orchestration**: Docker & Docker Compose

## Repository Directory Structure

```text
├── backend/                  # FastAPI Application
│   ├── app/
│   │   ├── api/              # Route handlers
│   │   ├── config/           # Pydantic settings loading
│   │   ├── database/         # Database sessions & engine config
│   │   ├── models/           # SQLAlchemy ORM models
│   │   ├── schemas/          # Pydantic schemas
│   │   ├── services/         # Business logic layer
│   │   └── utils/            # Global utilities
│   ├── main.py               # App entrypoint
│   ├── requirements.txt      # Dependency manifest
│   └── Dockerfile            # Container config
├── frontend/                 # React SPA
│   ├── src/                  # React source files
│   ├── package.json          # Frontend dependencies
│   ├── vite.config.js        # Vite settings (with backend api proxy)
│   └── Dockerfile            # Dev container config
├── docker-compose.yml        # Docker orchestration
├── .env.example              # Env config template
└── .cursorrules              # Architectural manifesto
```

## Running the Application

### 1. Configure the Environment
Copy the example environment file:
```bash
cp .env.example .env
```

### 2. Start the Pipeline using Docker Compose
```bash
docker-compose up --build
```
Once started:
- **Frontend**: `http://localhost:5173`
- **Backend API Docs**: `http://localhost:8000/docs`
- **Backend Health Check**: `http://localhost:8000/health`
