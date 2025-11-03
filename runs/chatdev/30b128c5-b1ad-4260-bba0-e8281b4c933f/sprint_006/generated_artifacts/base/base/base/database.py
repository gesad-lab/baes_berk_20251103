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
# Migration script to add Course table
def upgrade():
    from alembic import op
    import sqlalchemy as sa
    # Create the courses table
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False)
    )
def downgrade():
    from alembic import op
    op.drop_table('courses')  # Drop the courses table