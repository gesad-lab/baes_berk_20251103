'''
Handles the database migration to add the Teacher entity.
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
def migrate():
    '''
    Applies the migration to add the Teacher entity while preserving existing Student and Course data.
    '''
    engine = create_engine("sqlite:///./students.db")
    Base.metadata.bind = engine
    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()
    # Attempt to add the teacher_id column
    try:
        with engine.connect() as connection:
            connection.execute('ALTER TABLE courses ADD COLUMN teacher_id INTEGER;')
    except Exception as e:
        print(f"Column 'teacher_id' may already exist or another error occurred: {e}")
    Base.metadata.create_all(bind=engine)  # This will create the Teacher table without dropping existing data
    session.commit()
    session.close()