from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from alembic import op
import sqlalchemy as sa

# Base model for SQLAlchemy
Base = declarative_base()

# Migration script for creating the courses table
def upgrade():
    """Create the 'courses' table in the database."""
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('level', sa.String(length=50), nullable=False)
    )

def downgrade():
    """Drop the 'courses' table from the database."""
    op.drop_table('courses')