"""Add courses table and student_courses relationship table
Revision ID: xxxx
Revises: 
Create Date: 2023-10-01 12:00:00
"""
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'xxxx'
down_revision = None
branch_labels = None
depends_on = None
def upgrade():
    # Create the courses table
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    # Create the student_courses relationship table
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer(), nullable=False),
        sa.Column('course_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['student_id'], ['students.id'], ),
        sa.ForeignKeyConstraint(['course_id'], ['courses.id'], ),
        sa.PrimaryKeyConstraint('student_id', 'course_id')
    )
def downgrade():
    # Drop the student_courses table
    op.drop_table('student_courses')
    # Drop the courses table
    op.drop_table('courses')