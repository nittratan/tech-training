from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
from logger import logger

# Load environment variables
load_dotenv()

# Get database URL
DATABASE_URL = os.getenv('DATABASE_URL')

try:
    # Create SQLAlchemy engine
    engine = create_engine(DATABASE_URL)
    # Create a configured session class
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    logger.info("Database connection created successfully.")
except Exception as e:
    logger.error(f"Database connection failed: {e}")
    raise
