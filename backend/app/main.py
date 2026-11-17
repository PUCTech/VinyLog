from fastapi import FastAPI
from app.core.config import settings
from app.routers import dashboard

app = FastAPI(title=settings.app_name)
app.include_router(dashboard.router)

@app.get("/")
def teste():
    return {"status":"funcionando"}