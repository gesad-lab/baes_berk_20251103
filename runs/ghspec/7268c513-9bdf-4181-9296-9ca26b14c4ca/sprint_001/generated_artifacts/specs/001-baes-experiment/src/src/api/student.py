```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Student(db.Model):
    """Model representing a student."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

@app.before_first_request
def create_tables():
    """Create database tables on the first request."""
    db.create_all()

@app.route('/students', methods=['GET'])
def get_all_students():
    """Retrieve all students from the database."""
    students = Student.query.all()
    return jsonify([{'id': student.id, 'name': student.name} for student in students]), 200

@app.route('/students', methods=['POST'])
def create_student():
    """Create a new student in the database."""
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({
            'error': {
                'code': 'E001',
                'message': 'Name is required.'
            }
        }), 400

    new_student = Student(name=data['name'])
    db.session.add(new_student)
    db.session.commit()
    return jsonify({'id': new_student.id, 'name': new_student.name}), 201

if __name__ == '__main__':
    app.run(debug=True)
```