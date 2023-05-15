"""The configuration file for the app"""
import os
from typing import List

from dotenv import find_dotenv, load_dotenv
from pydantic import AnyHttpUrl, BaseSettings

load_dotenv(find_dotenv())


JWT_SECRET_KEY_ENV = os.environ.get("JWT_SECRET_KEY")
JWT_REFRESH_SECRET_KEY_ENV = os.environ.get("JWT_REFRESH_SECRET_KEY")
MONGODB_URL_ENV = os.environ.get("MONGODB_URL")

class Settings(BaseSettings):
    """The settings for the application

    Args:
        BaseSettings (Pydantic): The parent class for Settings
    """
    JWT_SECRET_KEY: str = JWT_SECRET_KEY_ENV
    JWT_REFRESH_SECRET_KEY: str = JWT_REFRESH_SECRET_KEY_ENV
    ALGORITHM = 'HS256'
    ACCESS_TOKEN_EXPIRATION_MINUTES: int = 15
    REFRESH_ACCESS_TOKEN_EXPIRATION_MINUTES: int = 60*24*7   # 7 days
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    
    # Database
    MONGODB_CONN_STRING = MONGODB_URL_ENV
    
    class Config: 
        """The configuration for the settings class"""
        case_sensitive = True
        

settings = Settings()
