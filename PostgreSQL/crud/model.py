from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import declarative_base

# Create a base class
Base = declarative_base()

# Define the Student model
class Student(Base):
    __tablename__ = 'std_info'
    __table_args__ = {'schema': 'std_data'}  # Specify schema name

    roll_no = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    department = Column(String(20))
    gender = Column(String(10))
    age = Column(Integer)
    phone = Column(String(15))
    city = Column(String(50))
    email = Column(String(100))
    # Auto-update timestamp on insert and update
    updated_ts = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())

