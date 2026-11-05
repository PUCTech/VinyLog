from pydantic_settings import BaseSettings

class VinyLogSettings(BaseSettings):
    app_name: str = "Teste"

settings = VinyLogSettings()