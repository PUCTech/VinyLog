from fastapi import FastAPI
from app.core.config import settings
from app.routers import users

app = FastAPI(title=settings.app_name)
app.include_router(users.router)

@app.get("/")
def teste():
    return {"status":"funcionando"}