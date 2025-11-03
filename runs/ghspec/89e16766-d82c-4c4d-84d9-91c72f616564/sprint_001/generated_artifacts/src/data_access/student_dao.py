class StudentDAO:
    def __init__(self):
        self.students = {}  # Store students by their ID

    def get_student(self, student_id: int) -> dict:
        """Retrieve a student by their unique ID.

        Args:
            student_id (int): The unique ID of the student to retrieve.

        Returns:
            dict: The student record if found, raises an Exception if not.

        Raises:
            ValueError: If the student ID is not found in records.
        """
        # Check if the student exists in the records
        if student_id not in self.students:
            raise ValueError(f"E001: Student with ID {student_id} not found.")
        
        return self.students[student_id]  # Return the found student record

    def create_student(self, student_id: int, name: str) -> None:
        """Create a new student record.

        Args:
            student_id (int): The unique ID of the student.
            name (str): The name of the student, which must not be empty.

        Raises:
            ValueError: If the name is empty or if the student already exists.
        """
        if not name:
            raise ValueError("E002: Student name cannot be empty.")
        if student_id in self.students:
            raise ValueError(f"E003: Student with ID {student_id} already exists.")
        
        # Store the student record
        self.students[student_id] = {"id": student_id, "name": name}  # Simple dict for student record