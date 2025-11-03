from alembic import op
from sqlalchemy import Column, Integer, ForeignKey


def upgrade():
    """Add teacher_id column to courses table."""
    op.add_column('courses', Column('teacher_id', Integer, ForeignKey('teachers.id'), nullable=True))


def downgrade():
    """Remove teacher_id column from courses table."""
    op.drop_column('courses', 'teacher_id')