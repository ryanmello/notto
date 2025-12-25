from fastapi import FastAPI
import uvicorn
from core.app import create_app

app = create_app()

def main():
    uvicorn.run(
        "main:app"
    )

if __name__ == "__main__":
    main()
