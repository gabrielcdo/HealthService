from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.settings import Settings

settings = Settings()

# Update the connection URL for PostgreSQL (hardcoded)
SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://:{settings.db_password}@{settings.db_host}:{settings.db_port}/{settings.db_name}"
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://meu_usuario:minha_senha@meu_postgres:5432/minha_database"
# Create engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# SessionLocal configuration
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declarative base
Base = declarative_base()

# Database session generator
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
