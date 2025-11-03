from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

@app.before_first_request
def create_tables():
    """Create database tables before the first request."""
    db.create_all()

@app.route('/students', methods=['POST'])
def create_student():
    """Create a new student record."""
    data = request.json
    if not data or 'name' not in data:
        return jsonify({"error": {"code": "E001", "message": "Name field is required."}}), 400
    
    new_student = Student(name=data['name'])
    db.session.add(new_student)
    db.session.commit()
    
    return jsonify({"id": new_student.id, "name": new_student.name}), 201

@app.route('/students', methods=['GET'])
def get_students():
    """Retrieve all student records."""
    students = Student.query.all()
    return jsonify([{"id": student.id, "name": student.name} for student in students]), 200

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint to monitor application status."""
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(debug=True)