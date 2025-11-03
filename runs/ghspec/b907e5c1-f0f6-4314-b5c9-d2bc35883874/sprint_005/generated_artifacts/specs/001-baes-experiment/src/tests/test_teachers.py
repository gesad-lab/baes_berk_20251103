```python
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from migrations import migrate_create_teachers_table
from models import Teacher

# Define a fixture to set up the database connection and migrate the table
@pytest.fixture(scope='module')
def db_setup():
    # Create a temporary in-memory SQLite database for testing
    engine = create_engine('sqlite:///test_database.db')
    Session = sessionmaker(bind=engine)
    
    # Create the tables if they don't exist
    migrate_create_teachers_table()

    # Create a session
    session = Session()
    
    yield session  # this will be the database session provided to tests
    
    # Cleanup - drop the teachers table after tests
    session.close()
    engine.dispose()

def test_create_teacher(db_setup):
    """Test the creation of a Teacher entity."""
    session = db_setup
    
    # Create a new Teacher instance
    new_teacher = Teacher(name='John Doe', email='john.doe@example.com')

    # Add and commit the new teacher to the session
    session.add(new_teacher)
    session.commit()

    # Verify the teacher was added successfully
    added_teacher = session.query(Teacher).filter_by(email='john.doe@example.com').first()
    assert added_teacher is not None
    assert added_teacher.name == 'John Doe'
    assert added_teacher.email == 'john.doe@example.com'

def test_create_teacher_with_invalid_email(db_setup):
    """Test creating a Teacher with an invalid email format raises an error."""
    session = db_setup
    invalid_teacher = Teacher(name='Jane Doe', email='invalid-email')

    session.add(invalid_teacher)
    
    with pytest.raises(Exception):
        session.commit()  # This should raise an error due to email format constraint

def test_retrieve_teacher(db_setup):
    """Test retrieving a Teacher entity by ID."""
    session = db_setup

    # Assuming we already have a valid teacher added in previous tests
    teacher = session.query(Teacher).filter_by(email='john.doe@example.com').first()

    # Retrieve using the primary key (id)
    retrieved_teacher = session.query(Teacher).get(teacher.id)

    assert retrieved_teacher is not None
    assert retrieved_teacher.name == 'John Doe'
    assert retrieved_teacher.email == 'john.doe@example.com'

def test_list_all_teachers(db_setup):
    """Test retrieving all Teacher entities."""
    session = db_setup

    # Create another teacher to confirm listing works
    new_teacher = Teacher(name='Alice Smith', email='alice.smith@example.com')
    session.add(new_teacher)
    session.commit()

    # Retrieve all teachers
    all_teachers = session.query(Teacher).all()
    
    assert len(all_teachers) >= 2  # At least one from the previous test and the new one
    assert any(teacher.name == 'Alice Smith' for teacher in all_teachers)
    assert any(teacher.name == 'John Doe' for teacher in all_teachers)
```