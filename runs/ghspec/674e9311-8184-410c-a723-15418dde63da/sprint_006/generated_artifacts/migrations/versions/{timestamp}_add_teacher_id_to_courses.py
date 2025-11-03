from alembic import op
from sqlalchemy import Column, Integer, ForeignKey

# Migration script to add teacher_id to courses table
def upgrade():
    """Add teacher_id column to the courses table."""
    op.add_column('courses', Column('teacher_id', Integer, ForeignKey('teachers.id'), nullable=True))

def downgrade():
    """Remove teacher_id column from the courses table."""
    op.drop_column('courses', 'teacher_id')