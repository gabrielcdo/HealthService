from typing import Optional

from pydantic_settings import BaseSettings
from app.core.singleton import singleton


@singleton
class Settings(BaseSettings):
    # API
    api_name:str = "banco_dados"
    api_version:str = "1.0.0"
    api_host:str = "0.0.0.0"
    api_port: int
    prefix:str = "/api"
    autoreload:bool = True

    environment:str = "local"

    db_host: str
    db_name: str
    db_user: str
    db_password: str
    db_port: int
    
    class Config:
        env_file = ".env"
