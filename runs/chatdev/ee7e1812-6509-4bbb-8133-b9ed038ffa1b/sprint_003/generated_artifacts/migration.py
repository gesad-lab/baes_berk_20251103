'''
Handles the database migration to add the Course entity.
'''
from sqlalchemy import create_engine
from models import Base
def migrate():
    '''
    Applies the migration to add the Course entity while preserving existing Student data.
    '''
    engine = create_engine("sqlite:///./students.db")
    Base.metadata.bind = engine
    Base.metadata.create_all(bind=engine)  # This will not drop existing data