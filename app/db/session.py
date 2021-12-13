import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

load_dotenv()
# Looks for postgres db in the environment variables
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')

# SQLALCHEMY_DATABASE_URI = "sqlite:///example.db"  # uncomment to use sqlite

engine = create_engine(SQLALCHEMY_DATABASE_URI)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
