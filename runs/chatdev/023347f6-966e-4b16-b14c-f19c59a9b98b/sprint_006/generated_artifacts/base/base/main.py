'''
Migration script to add Course table to the database.
'''
from sqlalchemy import create_engine, inspect
from models import Base  # Import Base from models to ensure all tables are created
DATABASE_URL = "sqlite:///./students.db"
def upgrade():
    engine = create_engine(DATABASE_URL)
    connection = engine.connect()
    inspector = inspect(engine)
    # Create all tables defined in Base if they don't exist
    Base.metadata.create_all(engine)
if __name__ == "__main__":
    upgrade()