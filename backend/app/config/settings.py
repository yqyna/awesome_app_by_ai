from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    project_name: str = "Awesome App API"
    version: str = "0.1.0"
    api_prefix: str = "/api"
    environment: str = "development"

    model_config = SettingsConfigDict(env_file=".env", env_prefix="APP_")


settings = Settings()
