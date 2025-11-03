from flask import Flask, request, jsonify
from models.student import db, Student

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Health Check Endpoint
@app.route('/health', methods=['GET'])
def health_check():
    """Health Check Endpoint."""
    response = {
        "status": "ok",
        "message": "Service is running",
    }
    return jsonify(response), 200

# POST Endpoint to create a new student
@app.route('/students', methods=['POST'])
def create_student():
    """Create a new student."""
    data = request.get_json()
    
    # Validate input
    if not data or 'name' not in data:
        return jsonify({"error": "E001: Invalid input. 'name' is required."}), 400
    
    new_student = Student(name=data['name'])
    db.session.add(new_student)
    db.session.commit()
    
    return jsonify({"message": "Student created successfully", "student": {"name": new_student.name}}), 201

# GET Endpoint to list all students
@app.route('/students', methods=['GET'])
def get_students():
    """Retrieve all students."""
    students = Student.query.all()
    return jsonify([{"name": student.name} for student in students]), 200

def initialize_db():
    """Initialize the SQLite database schema."""
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    initialize_db()  # Ensure the database schema is created on startup
    app.run(debug=True)