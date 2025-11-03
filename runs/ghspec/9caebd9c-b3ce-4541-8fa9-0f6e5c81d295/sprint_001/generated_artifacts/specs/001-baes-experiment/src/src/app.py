from flask import Flask, jsonify, request
from database import init_db
from validators import validate_student_name

app = Flask(__name__)

# Initialize the database
init_db(app)

@app.route('/students', methods=['POST'])
def create_student():
    """
    Create a new student entry.
    Request body must include 'name' as a JSON key.
    Returns the created student object on success.
    """
    data = request.get_json()
    
    # Validate the presence of 'name'
    name_validation_error = validate_student_name(data.get('name'))
    if name_validation_error:
        return jsonify(error={
            'code': 'E001',
            'message': name_validation_error
        }), 400
    
    # Here, you would add code to save the student to the database.
    # For example:
    # student = Student(name=data['name'])
    # db.session.add(student)
    # db.session.commit()
    
    return jsonify(student={'name': data['name']}), 201

@app.route('/students', methods=['GET'])
def get_students():
    """
    Retrieve all students.
    Returns a JSON list of student objects.
    """
    # Here, you would query the database for a list of students.
    # For example:
    # students = Student.query.all()
    # return jsonify(students=[student.name for student in students]), 200
    
    return jsonify(students=[]), 200  # Placeholder response for now

if __name__ == '__main__':
    app.run(debug=True)