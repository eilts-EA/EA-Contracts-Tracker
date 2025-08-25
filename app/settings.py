from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 480
    DATABASE_URL: str
    ADMIN_EMAIL: str = "admin@example.com"
    ADMIN_PASSWORD: str = "ChangeMe123!"

    SAM_API_KEY: str | None = None
    SAM_NAICS: str = "541330"
    SAM_SETASIDE: str = "SDVOSB"
    SAM_NOTICE_TYPES: str = "Presolicitation,Combined Synopsis/Solicitation"
    SAM_SYNC_INTERVAL_SECONDS: int = 21600

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()