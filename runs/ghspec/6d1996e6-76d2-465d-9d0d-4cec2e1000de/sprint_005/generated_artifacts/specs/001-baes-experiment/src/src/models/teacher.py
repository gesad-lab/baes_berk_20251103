class Teacher:
    def __init__(self, id: int, name: str, email: str):
        """
        Initialize a new Teacher instance.

        Args:
            id (int): Auto-generated primary key of the teacher.
            name (str): The name of the teacher, required.
            email (str): The email of the teacher, required.

        Raises:
            ValueError: If name or email is missing or invalid.
        """
        if not name:
            raise ValueError("E001: Name is required to create a teacher.")
        if not email:
            raise ValueError("E002: Email is required to create a teacher.")
        
        self.id = id              # auto-generated primary key
        self.name = name          # required string
        self.email = email        # required string
        
    def to_dict(self) -> dict:
        """
        Convert the Teacher instance to a dictionary format.

        Returns:
            dict: A dictionary representation of the teacher.
        """
        # Return the teacher details as a dictionary
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }