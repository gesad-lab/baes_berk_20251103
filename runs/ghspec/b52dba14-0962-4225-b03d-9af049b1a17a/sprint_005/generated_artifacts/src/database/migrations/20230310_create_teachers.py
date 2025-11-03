```python
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Teacher(Base):
    """Model representing a teacher in the database."""
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    def __repr__(self):
        return f"<Teacher(name={self.name}, email={self.email})>"

# SQLAlchemy setup (assuming a SQLite database for example)
DATABASE_URL = "sqlite:///teachers.db"  # Use environment variable in production
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

# Function to create a teacher
def create_teacher(name: str, email: str) -> dict:
    """Creates a new teacher in the database.

    Args:
        name (str): The name of the teacher.
        email (str): The email address of the teacher.

    Returns:
        dict: The created teacher details or error message if validation fails.
    """
    if not name or not email:
        return {"error": "Name and email are required."}

    if "@" not in email:  # Simplistic email validation
        return {"error": "Invalid email format."}

    new_teacher = Teacher(name=name, email=email)
    
    Session = sessionmaker(bind=engine)
    with Session() as session:
        session.add(new_teacher)
        session.commit()
        return {"message": "Teacher created successfully.", "teacher": {"name": new_teacher.name, "email": new_teacher.email}}

# Function to retrieve a teacher by ID
def get_teacher(teacher_id: int) -> dict:
    """Retrieves a teacher's details by their ID.

    Args:
        teacher_id (int): The ID of the teacher to retrieve.

    Returns:
        dict: The teacher's details or an error if not found.
    """
    Session = sessionmaker(bind=engine)
    with Session() as session:
        teacher = session.query(Teacher).filter_by(id=teacher_id).first()
        if teacher:
            return {"name": teacher.name, "email": teacher.email}
        else:
            return {"error": "Teacher not found."}
```