from pydantic_settings import BaseSettings, SettingsConfigDict

class VinyLogSettings(BaseSettings):
    app_name: str = "Teste"
    database_url: str
    model_config = SettingsConfigDict (
        env_file= "vinylog.env",
        env_file_encoding="utf-8"
    )

settings = VinyLogSettings()