'''
Handles database migrations for the Student and Course entities.
'''
from sqlalchemy import create_engine
from models import Base
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL)
def upgrade():
    # Create all tables if they do not exist
    Base.metadata.create_all(engine)
def downgrade():
    # Downgrade logic if needed
    pass
if __name__ == "__main__":
    upgrade()