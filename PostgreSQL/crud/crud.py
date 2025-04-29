from connection import SessionLocal
from model import Student
from sqlalchemy.exc import SQLAlchemyError
from logger import logger

class StudentCRUD:
    def __init__(self):
        self.db = SessionLocal()

    def create_student(self, student_data):
        try:
            student = Student(**student_data)
            self.db.add(student)
            self.db.commit()
            logger.info(f"Student inserted: {student_data}")
        except SQLAlchemyError as e:
            self.db.rollback()
            logger.error(f"Failed to insert student: {e}")

    def read_students(self):
        try:
            students = self.db.query(Student).all()
            logger.info("Fetched all students from database.")
            return students
        except SQLAlchemyError as e:
            logger.error(f"Failed to read students: {e}")
            return []

    def update_student(self, roll_no, updated_data):
        try:
            student = self.db.query(Student).filter(Student.roll_no == roll_no).first()
            if student:
                for key, value in updated_data.items():
                    setattr(student, key, value)
                self.db.commit()
                logger.info(f"Student updated: Roll No {roll_no}, Updates: {updated_data}")
            else:
                logger.warning(f"Student not found for update: Roll No {roll_no}")
        except SQLAlchemyError as e:
            self.db.rollback()
            logger.error(f"Failed to update student: {e}")

    def delete_student(self, roll_no):
        try:
            student = self.db.query(Student).filter(Student.roll_no == roll_no).first()
            if student:
                self.db.delete(student)
                self.db.commit()
                logger.info(f"Student deleted: Roll No {roll_no}")
            else:
                logger.warning(f"Student not found for deletion: Roll No {roll_no}")
        except SQLAlchemyError as e:
            self.db.rollback()
            logger.error(f"Failed to delete student: {e}")

    def __del__(self):
        self.db.close()
