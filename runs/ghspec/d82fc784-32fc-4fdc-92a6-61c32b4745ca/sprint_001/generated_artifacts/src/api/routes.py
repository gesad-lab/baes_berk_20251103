```python
from flask import Flask, jsonify, request
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.exc import NoResultFound
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set up the Flask app and database
app = Flask(__name__)
Base = declarative_base()
engine = create_engine('sqlite:///students.db')
Session = sessionmaker(bind=engine)
session = Session()

# Define the Student model
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

# Create the students table
Base.metadata.create_all(engine)

@app.route('/students', methods=['DELETE'])
def delete_student():
    student_id = request.args.get('id')
    if not student_id:
        logger.error("Student ID not provided")
        return jsonify({"error": {"code": "E001", "message": "Student ID is required"}}), 400
    
    try:
        student = session.query(Student).filter(Student.id == student_id).one()
        session.delete(student)
        session.commit()
        logger.info(f"Deleted student with ID {student_id}")
        return '', 204  # No Content
    except NoResultFound:
        logger.error(f"Student with ID {student_id} not found")
        return jsonify({"error": {"code": "E002", "message": "Student not found"}}), 404
    except Exception as e:
        logger.exception("An error occurred while deleting the student")
        return jsonify({"error": {"code": "E003", "message": "An unexpected error occurred"}}), 500

# Note: Implement other routes for handling students (Create, Retrieve, Update) accordingly
```