# Importing necessary modules from sqlalchemy

from sqlalchemy import create_engine  # Creates an engine that will communicate with the database and allow you to execute SQL queries
from sqlalchemy.ext.declarative import declarative_base # allows SQLAlchemy to know which classes are database models by creating a base class (Base)       
from sqlalchemy.orm import sessionmaker # Used to create a factory for creating new database sessions

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db" # Variable stores the connection URL for the database
engine = create_engine(SQLALCHEMY_DATABASE_URL) # Creates an engine for the database connection, using the URL
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # Creates a factory for database sessions
Base = declarative_base() # Defines the base class for your models

