class Student:
    """Represents a student in the system."""
    
    def __init__(self, name: str):
        """
        Initializes the Student instance.

        Parameters:
        - name (str): The name of the student. Must not be empty.

        Raises:
        - ValueError: If the name is empty.
        """
        if not name:
            raise ValueError("Name cannot be empty")
        self.name = name

    def __repr__(self):
        """Returns a string representation of the Student instance."""
        return f"Student(id={self.id}, name='{self.name}')"
    
    # Here, we might add methods related to database interaction in the future.
    # For now, the class serves to encapsulate student-related data and validation.