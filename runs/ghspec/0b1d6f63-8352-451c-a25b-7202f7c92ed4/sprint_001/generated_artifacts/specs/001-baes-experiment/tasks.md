# Tasks: Student Management Web Application

## Task 1: Setup Development Environment
- **File Path**: `requirements.txt`
- **Task**: Create a `requirements.txt` file with the following content:
  ```
  Flask
  SQLAlchemy
  Flask-Migrate
  pytest
  ```

## Task 2: Create Project Structure
- **File Path**: `StudentManagement/`
- **Task**: Create the following folder structure:
  ```
  StudentManagement/
  ├── src/
  ├── tests/
  ├── requirements.txt
  └── README.md
  ```

## Task 3: Initialize Flask Application
- **File Path**: `src/app.py`
- **Task**: Implement the initial structure of the Flask application in `app.py`:
  ```python
  from flask import Flask
  
  app = Flask(__name__)
  
  if __name__ == "__main__":
      app.run(debug=True)
  ```

## Task 4: Define SQLAlchemy Models
- **File Path**: `src/models.py`
- **Task**: Define the SQLAlchemy model for the Student entity:
  ```python
  from flask_sqlalchemy import SQLAlchemy

  db = SQLAlchemy()

  class Student(db.Model):
      id = db.Column(db.Integer, primary_key=True, autoincrement=True)
      name = db.Column(db.String, nullable=False)
  ```

## Task 5: Configure SQLAlchemy with Flask
- **File Path**: `src/app.py`
- **Task**: Add SQLAlchemy configuration to `app.py` and initialize it:
  ```python
  from flask import Flask
  from models import db
  
  app = Flask(__name__)
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
  db.init_app(app)
  ```

## Task 6: Set Up Routes for API Endpoints
- **File Path**: `src/routes.py`
- **Task**: Create the file and define the routes for creating and retrieving student records:
  ```python
  from flask import Flask, request, jsonify
  from models import db, Student

  app = Flask(__name__)

  @app.route('/students', methods=['POST'])
  def create_student():
      # Implementation will be added in a later task
      pass

  @app.route('/students/<int:id>', methods=['GET'])
  def get_student(id):
      # Implementation will be added in a later task
      pass
  ```

## Task 7: Implement Creating a Student Record
- **File Path**: `src/routes.py`
- **Task**: Implement the logic to create a student record in `create_student()`:
  ```python
      data = request.get_json()
      name = data.get("name")
      if not name:
          return jsonify({"error": {"code": "E001", "message": "Name is required"}}), 400
      new_student = Student(name=name)
      db.session.add(new_student)
      db.session.commit()
      return jsonify({"message": "Student created successfully", "id": new_student.id}), 201
  ```

## Task 8: Implement Retrieving a Student Record
- **File Path**: `src/routes.py`
- **Task**: Implement the logic to retrieve a student record in `get_student()`:
  ```python
      student = Student.query.get(id)
      if student is None:
          return jsonify({"error": {"code": "E002", "message": "Student not found"}}), 404
      return jsonify({"id": student.id, "name": student.name}), 200
  ```

## Task 9: Create Database Tables on Startup
- **File Path**: `src/app.py`
- **Task**: Ensure the database tables are created on startup by adding:
  ```python
  with app.app_context():
      db.create_all()
  ```

## Task 10: Implement Testing for API Endpoints
- **File Path**: `tests/test_routes.py`
- **Task**: Set up tests for the API endpoints by creating test cases:
   ```python
   import pytest
   from src.app import app
   
   @pytest.fixture
   def client():
       with app.test_client() as client:
           yield client

   def test_create_student(client):
       response = client.post('/students', json={"name": "John Doe"})
       assert response.status_code == 201
       assert 'id' in response.get_json()

   def test_get_student(client):
       response = client.post('/students', json={"name": "Jane Doe"})
       student_id = response.get_json()['id']
       response = client.get(f'/students/{student_id}')
       assert response.status_code == 200
       assert 'Jane Doe' == response.get_json()['name']

   def test_create_student_no_name(client):
       response = client.post('/students', json={})
       assert response.status_code == 400
       assert response.get_json()['error']['message'] == 'Name is required'
   ```

## Task 11: Write Project Documentation
- **File Path**: `README.md`
- **Task**: Provide setup instructions, usage, and API details in the `README.md`.

## Task 12: Implement Logging
- **File Path**: `src/app.py`
- **Task**: Add basic logging configuration to `app.py` using Python's built-in logging:
  ```python
  import logging

  logging.basicConfig(level=logging.INFO)
  ```

## Task 13: Conduct a Smoke Test
- **File Path**: `tests/test_routes.py`
- **Task**: After implementation, run all tests to verify that the application behaves as expected.