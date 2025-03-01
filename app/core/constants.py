import os

from app.core.settings import Settings


class Stage:
    PROD = "prod"
    DEV = "dev"
    LOCAL = "local"
    TEST = "test"


HOST = "0.0.0.0"
PREFIX = "/api/banco_dados"
