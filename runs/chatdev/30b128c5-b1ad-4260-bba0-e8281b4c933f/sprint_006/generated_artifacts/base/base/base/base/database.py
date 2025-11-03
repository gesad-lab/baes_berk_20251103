'''
Handles database connection and session management.
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models import Base
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# Migration script to add email column
def upgrade():
    from alembic import op
    import sqlalchemy as sa
    # Step 1: Add email column as nullable
    op.add_column('students', sa.Column('email', sa.String(), nullable=True))
    # Step 2: Update existing records to have a default email value
    connection = op.get_bind()
    connection.execute("UPDATE students SET email = '' WHERE email IS NULL")
    # Step 3: Alter the column to be non-nullable
    op.alter_column('students', 'email', nullable=False)
def downgrade():
    from alembic import op
    op.drop_column('students', 'email')