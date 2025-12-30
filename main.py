from fastapi import FastAPI
import uvicorn
from uvicorn.config import LOG_LEVELS
from core.app import create_app
from config.settings import settings

app = create_app()

def main():
    print(f"   Starting {settings.PROJECT_NAME}")
    print(f"   Host: {settings.HOST}")
    print(f"   Port: {settings.PORT}")
    print(f"   Reload: {settings.RELOAD}")
    print(f"   API Docs: http://{settings.HOST}:{settings.PORT}/docs")
    
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.RELOAD,
        log_level=settings.LOG_LEVEL,
        access_log=True,
    )

if __name__ == "__main__":
    main()
