from model import Base
from connection import engine
from crud import StudentCRUD
from logger import logger

# Create tables if they don't exist
try:
    Base.metadata.create_all(bind=engine)
    logger.info("Database tables created successfully (if not exists).")
except Exception as e:
    logger.error(f"Error creating tables: {e}")
    raise

def main():
    crud = StudentCRUD()

    # Example student data
    student_data = {
        "roll_no": 700,
        "name": "Pragya",
        "department": "HR",
        "gender": "female",
        "age": 26,
        "phone": "90123333000",
        "city": "Gurugram",
        "email": "pragya@nitt.edu"
    }

    # Insert a student
    crud.create_student(student_data)

    # Read all students
    students = crud.read_students()
    for s in students:
        print(f"{s.roll_no} - {s.name} - {s.department}")

    # Update student information
    crud.update_student(700, {"city": "Hyderabad", "phone": "9111111111"})

    # Delete student
    # crud.delete_student(601)

if __name__ == "__main__":
    main()
