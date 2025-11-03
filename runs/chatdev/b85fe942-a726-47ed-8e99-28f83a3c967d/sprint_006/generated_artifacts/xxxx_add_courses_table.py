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
    # Create the teachers table
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    # Add teacher_id column to courses table without foreign key constraint
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))  # Nullable for existing data
    # Here you can add logic to populate teacher_id if necessary, e.g., setting a default teacher for existing courses
    # Now, alter the column to add the foreign key constraint
    op.create_foreign_key('fk_teacher', 'courses', 'teachers', ['teacher_id'], ['id'])
def downgrade():
    # Drop the teacher_id column from courses table
    op.drop_column('courses', 'teacher_id')
    # Drop the teachers table
    op.drop_table('teachers')
    # Drop the student_courses table
    op.drop_table('student_courses')
    # Drop the courses table
    op.drop_table('courses')