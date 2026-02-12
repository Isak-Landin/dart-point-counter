from fastapi import FastAPI
from .routes import router

app = FastAPI(title="Dart Backend MVP")

app.include_router(router)


if __name__ == "__main__":
    
