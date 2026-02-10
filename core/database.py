from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql+psycopg2://auth_user:123456@localhost:5432/postgres"

engine = create_engine(
    DATABASE_URL,
    echo=True,
    connect_args={"options": "-csearch_path=auth"}  # ← quan trọng
)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()
