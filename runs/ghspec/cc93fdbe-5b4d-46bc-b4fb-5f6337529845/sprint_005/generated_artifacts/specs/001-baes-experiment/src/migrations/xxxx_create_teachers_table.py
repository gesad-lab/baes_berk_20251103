```python
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, DDL
from sqlalchemy.orm import sessionmaker

# Create a Base for the migration
Base = declarative_base(metadata=MetaData())

class Teacher(Base):
    """Representation of the Teacher table in the database."""
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)


def upgrade():
    """Apply the migration to create the teachers table."""
    # Create the table with constraints
    Base.metadata.create_all(bind=engine)


def downgrade():
    """Revert the migration by dropping the teachers table."""
    # Drop the table if it exists
    Teacher.__table__.drop(bind=engine)


# Database setup for migration execution
DATABASE_URL = "sqlite:///./test.db"  # Change this to your actual database URL
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

if __name__ == "__main__":
    with Session() as session:
        # Execute the upgrade function to create the table
        upgrade()
```
