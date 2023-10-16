"""Database Functions"""

# General Imports
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


user_name = "postgres"
password = "passw0rd"
address = "postgres_container_2"
port = 5432
db_name = "postgres"
DATABASE_URL = f"postgresql://{user_name}:{password}@{address}:{port}/{db_name}"


engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
Base.metadata.schema = "grocery_app"


def get_db_connection():
    """Function to get DB Connection"""

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
