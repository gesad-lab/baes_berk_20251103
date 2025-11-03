```python
import unittest
from app import create_app, db
from models import Student

class TestStudentService(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up the test environment and create the application."""
        cls.app = create_app()
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        db.create_all()  # Create the schema before running tests

    @classmethod
    def tearDownClass(cls):
        """Clean up the database after tests are done."""
        db.session.remove()
        db.drop_all()  # Drop the schema after running tests
        cls.app_context.pop()

    def test_schema_creation_on_startup(self):
        """Test that the database schema is created on startup."""
        # Check if the Student table exists in the database
        table_exists = 'student' in db.metadata.tables
        self.assertTrue(table_exists, "The 'student' table was not created.")

    def test_create_student(self):
        """Test creating a new student record."""
        with self.app.test_client() as client:
            response = client.post('/students', json={'name': 'John Doe'})
            self.assertEqual(response.status_code, 201)
            self.assertIn('name', response.get_json())
            self.assertEqual(response.get_json()['name'], 'John Doe')

    def test_get_student_by_id(self):
        """Test retrieving a student record by ID."""
        student = Student(name='Jane Doe')
        db.session.add(student)
        db.session.commit()

        with self.app.test_client() as client:
            response = client.get(f'/students/{student.id}')
            self.assertEqual(response.status_code, 200)
            self.assertIn('name', response.get_json())
            self.assertEqual(response.get_json()['name'], 'Jane Doe')

    def test_list_all_students(self):
        """Test listing all student records."""
        student1 = Student(name='Alice')
        student2 = Student(name='Bob')
        db.session.add_all([student1, student2])
        db.session.commit()

        with self.app.test_client() as client:
            response = client.get('/students')
            self.assertEqual(response.status_code, 200)
            students = response.get_json()
            self.assertEqual(len(students), 2)  # Expecting two students
            self.assertIn('Alice', [student['name'] for student in students])
            self.assertIn('Bob', [student['name'] for student in students])

if __name__ == '__main__':
    unittest.main()
```