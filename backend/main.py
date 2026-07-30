from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config.settings import settings

app = FastAPI(
    title="InsightBridge API",
    description="Business Intelligence Sentiment Analysis Pipeline API",
    version="1.0.0",
)

# Configure CORS dynamically based on Pydantic Settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health", tags=["health"])
async def health_check():
    """
    Health check endpoint to verify backend service running state.
    """
    return {"status": "ok", "app": "InsightBridge API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host=settings.HOST, port=settings.PORT, reload=True)
