from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    APP_NAME : str = "TO-DO REST API"
    API_V1_STR : str = "/api/v1"

    # JWT
    SECRET_KEY : str = "supersecret"
    ALGORITHM : str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES : int = 60

    # DATABASE
    DATABASE_URL : str = "sqlite:///./todo.db"

    class Config:
        env_file = ".env"

settings = Settings()

