from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student  # Assuming a Student model exists in models.py
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Database setup
DATABASE_URL = "sqlite:///students.db"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)  # Creates the table if it doesn't exist
Session = sessionmaker(bind=engine)

app = Flask(__name__)

@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    logger.info("Creating a new student record: %s", data)

    if not data or 'name' not in data:
        logger.warning("Invalid request payload: %s", data)
        return jsonify({"error": "E001: Invalid request payload"}), 400
    
    # Create a new student
    session = Session()
    try:
        new_student = Student(name=data['name'])
        session.add(new_student)
        session.commit()
        logger.info("Student created successfully: %s", new_student.id)
        return jsonify({"id": new_student.id, "name": new_student.name}), 201
    except Exception as e:
        logger.error("Failed to create student: %s", e)
        session.rollback()
        return jsonify({"error": "E002: Could not create student"}), 500
    finally:
        session.close()

@app.route('/students', methods=['GET'])
def retrieve_students():
    logger.info("Retrieving student records")
    
    session = Session()
    try:
        students = session.query(Student).all()
        student_list = [{"id": student.id, "name": student.name} for student in students]
        logger.info("Retrieved %d students", len(student_list))
        return jsonify(student_list), 200
    except Exception as e:
        logger.error("Failed to retrieve students: %s", e)
        return jsonify({"error": "E003: Could not retrieve students"}), 500
    finally:
        session.close()

@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.get_json()
    logger.info("Updating student record (ID: %d) with data: %s", id, data)

    if not data or 'name' not in data:
        logger.warning("Invalid request payload: %s", data)
        return jsonify({"error": "E001: Invalid request payload"}), 400

    session = Session()
    try:
        student = session.query(Student).filter(Student.id == id).one_or_none()
        if student is None:
            logger.warning("Student not found (ID: %d)", id)
            return jsonify({"error": "E004: Student not found"}), 404
        
        student.name = data['name']
        session.commit()
        logger.info("Student updated successfully (ID: %d)", id)
        return jsonify({"id": student.id, "name": student.name}), 200
    except Exception as e:
        logger.error("Failed to update student (ID: %d): %s", id, e)
        session.rollback()
        return jsonify({"error": "E005: Could not update student"}), 500
    finally:
        session.close()

@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    logger.info("Deleting student record (ID: %d)", id)

    session = Session()
    try:
        student = session.query(Student).filter(Student.id == id).one_or_none()
        if student is None:
            logger.warning("Student not found for deletion (ID: %d)", id)
            return jsonify({"error": "E004: Student not found"}), 404
        
        session.delete(student)
        session.commit()
        logger.info("Student deleted successfully (ID: %d)", id)
        return '', 204
    except Exception as e:
        logger.error("Failed to delete student (ID: %d): %s", id, e)
        session.rollback()
        return jsonify({"error": "E006: Could not delete student"}), 500
    finally:
        session.close()

if __name__ == '__main__':
    app.run(debug=True)