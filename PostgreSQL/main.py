from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

# Tumhari PostgreSQL connection string yaha daalo
# Example: 'postgresql://username:password@localhost:5432/databasename'
DATABASE_URL = "postgresql://test_db_gagt_user:5Wk4xT3nGM4liaqQlpcwheVX9Pyeg5le@dpg-d07mo3hr0fns738nmumg-a.oregon-postgres.render.com/test_db_gagt"

def check_connection():
    """
    Check if connection to PostgreSQL database is successful
    
    Args:
        connection_string (str): SQLAlchemy connection string for PostgreSQL
        
    Returns:
        tuple: (bool: connection status, str: message)
    """
    try:
        # connection create
        engine = create_engine(DATABASE_URL)
        
        # Connection open and close
        # This will raise an error if the connection fails
        with engine.connect() as connection:
            print("✅ Database connected successfully!")
    
    except SQLAlchemyError as e:
        print("❌ Database connection failed!")
        print(f"Error: {e}")

if __name__ == "__main__":
    check_connection()
