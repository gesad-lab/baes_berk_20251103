"""Add_courses_to_student

Revision ID: xxx_revisions
Revises: previous_revision_id
Create Date: YYYY-MM-DD
"""
from alembic import op
import sqlalchemy as sa

def upgrade():
    # Altering the 'student' table to create a new table for course relationships
    # This will also enforce referential integrity.
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer(), nullable=False),
        sa.Column('course_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['student_id'], ['student.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['course_id'], ['course.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('student_id', 'course_id')
    )

def downgrade():
    # Dropping the student_courses table to revert schema changes
    op.drop_table('student_courses')