```python
import sqlite3

class Student:
    """A class to represent a student with a name."""

    def __init__(self, name: str):
        self.name = name

    def save(self):
        """Saves the student record to the database."""
        with sqlite3.connect('students.db') as conn:
            cursor = conn.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT)")
            cursor.execute("INSERT INTO students (name) VALUES (?)", (self.name,))
            conn.commit()

    @classmethod
    def get_by_id(cls, student_id: int):
        """Retrieves a student record by its ID."""
        with sqlite3.connect('students.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM students WHERE id = ?", (student_id,))
            result = cursor.fetchone()
            return cls(result[0]) if result else None

# pytest test functions for testing the Student management functionality

def test_student_creation():
    """Test the creation of a student record."""
    student = Student("John Doe")
    student.save()
    
    # Check if the student is saved correctly
    retrieved_student = Student.get_by_id(1)  # Assuming this is the first student saved
    assert retrieved_student is not None
    assert retrieved_student.name == "John Doe"

def test_student_retrieval_nonexistent_id():
    """Test retrieval for a nonexistent student ID."""
    student = Student.get_by_id(999)  # Nonexistent ID
    assert student is None
```