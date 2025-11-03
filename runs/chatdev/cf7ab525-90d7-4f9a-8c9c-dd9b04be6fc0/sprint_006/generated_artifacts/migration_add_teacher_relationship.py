'''
Migration script to add teacher_id column to the courses table.
'''
from sqlalchemy import Column, Integer, ForeignKey
from alembic import op
def upgrade():
    op.add_column('courses', Column('teacher_id', Integer, ForeignKey('teachers.id')))  # Add this line
def downgrade():
    op.drop_column('courses', 'teacher_id')