from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {"id": self.id, "name": self.name}

# Initialize the database and create tables
with app.app_context():
    db.create_all()

@app.route('/api/students', methods=['POST'])
def create_student():
    """Create a new student"""
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({"error": "E001: Name is required"}), 400
    
    new_student = Student(name=data['name'])
    db.session.add(new_student)
    db.session.commit()
    
    return jsonify(new_student.to_dict()), 201

@app.route('/api/students/<int:student_id>', methods=['GET'])
def retrieve_student(student_id):
    """Retrieve a student's details by ID"""
    student = Student.query.get(student_id)
    if student is None:
        return jsonify({"error": "E002: Student not found"}), 404
    
    return jsonify(student.to_dict()), 200

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint to monitor application health"""
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    # Ensure that the application starts with minimal setup
    debug_mode = os.getenv('DEBUG_MODE', 'false').lower() == 'true'
    app.run(debug=debug_mode)  # Run the app in debug mode if specified
