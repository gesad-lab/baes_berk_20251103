from sqlalchemy import Column, Integer, String

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    
    # Email field added to store unique email addresses of students.
    # This field is required to ensure that every student has a valid email
    # address, which facilitates effective communication and data management.
    # Additionally, it is marked as unique to prevent duplicate email entries
    # in the database, thus maintaining data integrity.
    email = Column(String, nullable=False, unique=True)

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}', email='{self.email}'>"