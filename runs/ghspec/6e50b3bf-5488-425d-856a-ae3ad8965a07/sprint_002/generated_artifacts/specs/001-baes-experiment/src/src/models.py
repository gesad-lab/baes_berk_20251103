class Student:
    """
    Represents a student in the system.
    
    Attributes:
        id (int): Auto-incremented primary key for the student.
        name (str): Name of the student (non-nullable).
        email (str): Email of the student (non-nullable). Must be a valid email format.
    """
    
    def __init__(self, id: int, name: str, email: str):
        if not self.is_valid_email(email):
            raise ValueError(f"Invalid email format: {email}")
        self.id = id
        self.name = name
        self.email = email

    @staticmethod
    def is_valid_email(email: str) -> bool:
        """
        Validates the email format.
        
        Args:
            email (str): Email address to validate.
        
        Returns:
            bool: True if the email is valid, else False.
        """
        import re
        email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        return re.match(email_regex, email) is not None

    def __repr__(self) -> str:
        return f"Student(id={self.id}, name='{self.name}', email='{self.email}')"