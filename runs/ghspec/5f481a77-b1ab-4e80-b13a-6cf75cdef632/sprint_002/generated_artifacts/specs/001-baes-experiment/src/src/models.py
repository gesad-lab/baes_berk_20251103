class Student:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email  # Added email attribute to the Student class

    def __repr__(self):
        return f"<Student(name={self.name}, email={self.email})>"

    # You may add any necessary methods related to Student behavior here


# Additional methods or functions as needed can be placed below this comment.