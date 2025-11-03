'''
Handles database migrations for the Student entity.
'''
from sqlalchemy import create_engine, text
from models import Base
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL)
def upgrade():
    # Create all tables if they do not exist
    Base.metadata.create_all(engine)
    with engine.connect() as connection:
        # Check if the 'email' column exists
        result = connection.execute(text("PRAGMA table_info(students)"))
        columns = [row[1] for row in result]
        if 'email' not in columns:
            connection.execute(text('ALTER TABLE students ADD COLUMN email TEXT NOT NULL'))
def downgrade():
    # Downgrade logic if needed
    pass
if __name__ == "__main__":
    upgrade()