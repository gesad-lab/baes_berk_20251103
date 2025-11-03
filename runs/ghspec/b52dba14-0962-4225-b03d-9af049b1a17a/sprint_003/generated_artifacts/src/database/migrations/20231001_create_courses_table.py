from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer

def upgrade():
    """Create the courses table in the database."""
    engine = create_engine('sqlite:///path_to_your_db')  # Update with the actual database URL
    metadata = MetaData(bind=engine)
    
    # Define the 'courses' table schema
    courses = Table('courses', metadata,
                    Column('id', Integer, primary_key=True, autoincrement=True),
                    Column('name', String, nullable=False),  # Mandatory field for course name
                    Column('level', String, nullable=False)  # Mandatory field for course level
                   )
    
    # Create the table in the database
    metadata.create_all(engine)

def downgrade():
    """Drop the courses table from the database."""
    engine = create_engine('sqlite:///path_to_your_db')  # Update with the actual database URL
    metadata = MetaData(bind=engine)
    courses = Table('courses', metadata, autoload_with=engine)
    
    # Drop the 'courses' table if it exists
    courses.drop(engine)