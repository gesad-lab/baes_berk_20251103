```python
# services/teacher_service.py

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.exc import IntegrityError
from pydantic import BaseModel, EmailStr
from typing import Optional

# Database setup - adjust connection as needed
DATABASE_URL = 'sqlite:///courses.db'
engine = create_engine(DATABASE_URL)
metadata = MetaData(bind=engine)

# Teacher table definition
teachers_table = Table('teachers', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String, nullable=False),
    Column('email', String, nullable=False)
)

# Create Pydantic model for Teacher
class TeacherCreate(BaseModel):
    name: str
    email: EmailStr

class TeacherResponse(BaseModel):
    id: int
    name: str
    email: str

def create_teacher(teacher_data: TeacherCreate) -> TeacherResponse:
    """Create a new teacher in the database."""
    try:
        with engine.connect() as connection:
            result = connection.execute(teachers_table.insert().values(
                name=teacher_data.name,
                email=teacher_data.email
            ))
            teacher_id = result.inserted_primary_key[0]  # Get the generated ID
            return TeacherResponse(id=teacher_id, name=teacher_data.name, email=teacher_data.email)
    except IntegrityError as e:
        # Handle integrity error if email already exists
        raise ValueError("A teacher with this email already exists.") from e

def get_teacher(teacher_id: int) -> Optional[TeacherResponse]:
    """Retrieve a teacher by their ID."""
    with engine.connect() as connection:
        result = connection.execute(teachers_table.select().where(teachers_table.c.id == teacher_id))
        teacher = result.fetchone()
        if teacher:
            return TeacherResponse(id=teacher.id, name=teacher.name, email=teacher.email)
        return None  # Teacher not found
```