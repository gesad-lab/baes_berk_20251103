from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String

# Initialize the Flask application
app = Flask(__name__)

# Database configuration (this should be replaced with environment variables or configuration management in production)
DATABASE_URL = "sqlite:///students.db"

# SQLAlchemy settings
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Student model
class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

# Automatic database schema creation
def init_db():
    # Create tables if they don't exist yet
    Base.metadata.create_all(bind=engine)

# Routes for student management
@app.route('/students', methods=['POST'])
def create_student():
    data = request.json
    if 'name' not in data:
        return jsonify({"error": {"code": "E001", "message": "Name is required."}}), 400
    
    new_student = Student(name=data['name'])
    db = SessionLocal()
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    db.close()
    
    return jsonify({"id": new_student.id, "name": new_student.name}), 201

@app.route('/students', methods=['GET'])
def get_students():
    db = SessionLocal()
    students = db.query(Student).all()
    db.close()
    return jsonify([{"id": student.id, "name": student.name} for student in students]), 200

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    init_db()  # Ensure the database schema is created automatically
    app.run(debug=True)  # Start the application without needing manual intervention