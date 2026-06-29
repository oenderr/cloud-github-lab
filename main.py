from fastapi import FastAPI
import platform
import os
from datetime import datetime

app = FastAPI(
    title="Simple FastAPI Cloud Project",
    description="A minimal FastAPI application for demonstration and portfolio purposes.",
    version="0.1.0",
)

@app.get("/health")
async def health_check():
    """
    Health check endpoint to verify the service is running.
    Returns a simple status message.
    """
    return {"status": "healthy", "timestamp": datetime.utcnow().isoformat()}

@app.get("/info")
async def info():
    """
    Information endpoint providing details about the application and environment.
    """
    return {
        "app_name": app.title,
        "app_version": app.version,
        "python_version": platform.python_version(),
        "platform": platform.platform(),
        "environment": os.getenv("ENVIRONMENT", "development"),
        "timestamp": datetime.utcnow().isoformat(),
    }

if __name__ == "__main__":
    # This block is for running the app directly with Uvicorn for development
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)