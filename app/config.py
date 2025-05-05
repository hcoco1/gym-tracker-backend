from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    database_url: str

    class Config:
        env_file = ".env"
        extra = "ignore"  # Ignore extra env variables

settings = Settings()