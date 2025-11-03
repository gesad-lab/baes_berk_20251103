from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db = SQLAlchemy(app)

class Student(db.Model):
    """Represents a student record in the database."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        """Convert the Student to a dictionary for JSON serialization."""
        return {
            "id": self.id,
            "name": self.name
        }

@app.before_first_request
def create_tables():
    """Creates the database tables before the first request."""
    db.create_all()

@app.route('/students', methods=['POST'])
def create_student():
    """Create a new student record."""
    data = request.get_json()
    
    # Validate input
    if not data or 'name' not in data or not data['name']:
        return jsonify({"error": {"code": "E001", "message": "Name is required."}}), 400

    new_student = Student(name=data['name'])
    try:
        db.session.add(new_student)
        db.session.commit()
        return jsonify({
            "message": "Student created successfully.",
            "student_id": new_student.id
        }), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": {"code": "E002", "message": "Failed to create student."}}), 500
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": {"code": "E003", "message": str(e)}}), 500

@app.route('/students/<identifier>', methods=['GET'])
def get_student(identifier):
    """Retrieve a student by ID or name."""
    student = None
    
    # Check if identifier is an integer (ID) or a name
    if identifier.isdigit():
        student = Student.query.get(identifier)
    else:
        student = Student.query.filter_by(name=identifier).first()

    if student is None:
        return jsonify({"error": {"code": "E004", "message": "Student not found."}}), 404

    return jsonify(student.to_dict()), 200

if __name__ == '__main__':
    app.run(debug=True)