from flask import Flask
from flask_restplus import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version='1.0', title='Student Management API',
          description='An API for managing students in the Student Management Application')

# Define the Student model
student_model = api.model('Student', {
    'name': fields.String(required=True, description='The name of the student'),
    'email': fields.String(required=True, description='The email of the student, required for communication and data integrity'),
})

# API endpoint for creating a new student
@api.route('/students')
class StudentList(Resource):
    @api.expect(student_model)
    def post(self):
        """Create a new student"""
        # Code to create a student would go here
        return {'message': 'Student created successfully.'}, 201

    def get(self):
        """Retrieve a list of all students"""
        # Code to retrieve students would go here
        return [{'name': 'John Doe', 'email': 'john.doe@example.com'}], 200

# API endpoint for retrieving a student by ID
@api.route('/students/<int:id>')
class Student(Resource):
    def get(self, id):
        """Retrieve a student by ID"""
        # Code to get a student by ID would go here
        return {'name': 'John Doe', 'email': 'john.doe@example.com'}, 200

if __name__ == '__main__':
    app.run(debug=True)