class Student:
    """
    Represents a student entity within the system.
    
    Attributes:
        name (str): The name of the student.
        email (str): The email address of the student.
    """
    
    def __init__(self, name: str, email: str):
        """
        Initializes a new Student instance.
        
        Args:
            name (str): The name of the student.
            email (str): The email address of the student.
        """
        self.name = name
        self.email = email
    
    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not value:
            raise ValueError("Name cannot be empty.")
        self._name = value

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str) -> None:
        if not value:
            raise ValueError("Email cannot be empty.")
        self._email = value

    def __repr__(self) -> str:
        return f"<Student(name={self.name}, email={self.email})>"