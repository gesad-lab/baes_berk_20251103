from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from database import initialize_db
from services import create_student, get_students

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Automatically initialize the database and create tables on startup
initialize_db(app)

@app.route('/students', methods=['POST'])
def add_student():
    """Create a new student record."""
    data = request.get_json()
    
    # Validate input
    if not data or 'name' not in data:
        return jsonify({"error": {"code": "E001", "message": "Name is required."}}), 400
    
    # Create student and return the result
    student = create_student(data['name'])
    return jsonify({
        "id": student.id,
        "name": student.name
    }), 201

@app.route('/students', methods=['GET'])
def retrieve_students():
    """Retrieve a list of all students."""
    students = get_students()
    return jsonify([{"id": student.id, "name": student.name} for student in students]), 200

if __name__ == '__main__':
    app.run(debug=True)