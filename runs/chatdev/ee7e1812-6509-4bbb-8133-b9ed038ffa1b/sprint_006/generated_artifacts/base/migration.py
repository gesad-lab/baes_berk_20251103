'''
Handles the database migration to add the Teacher entity.
'''
from sqlalchemy import create_engine
from models import Base
def migrate():
    '''
    Applies the migration to add the Teacher entity while preserving existing Student and Course data.
    '''
    engine = create_engine("sqlite:///./students.db")
    Base.metadata.bind = engine
    Base.metadata.create_all(bind=engine)  # This will create the Teacher table without dropping existing data