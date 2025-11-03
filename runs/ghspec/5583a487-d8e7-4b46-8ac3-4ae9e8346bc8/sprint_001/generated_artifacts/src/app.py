```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import os

app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Student model for the database
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

# Function to create the database schema on startup
def create_database():
    try:
        db.create_all()  # Creates database tables
        print("Database created successfully.")
    except Exception as e:
        print(f"Error creating database: {e}")

@app.route('/students', methods=['POST'])
def create_student():
    """Creates a new student record."""
    data = request.get_json()
    
    if not data or 'name' not in data:
        return jsonify({"error": {"code": "E001", "message": "Name field is required."}}), 400

    new_student = Student(name=data['name'])
    
    try:
        db.session.add(new_student)
        db.session.commit()
        return jsonify({"message": "Student created successfully."}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": {"code": "E002", "message": "Student already exists."}}), 400
    except Exception as e:
        return jsonify({"error": {"code": "E003", "message": f"An error occurred: {e}"}}), 500

@app.route('/students', methods=['GET'])
def get_students():
    """Retrieves all student records."""
    students = Student.query.all()
    return jsonify([{"id": student.id, "name": student.name} for student in students]), 200

if __name__ == '__main__':
    create_database()  # Ensure database is created on startup
    app.run(debug=True)  # Start the Flask application
```