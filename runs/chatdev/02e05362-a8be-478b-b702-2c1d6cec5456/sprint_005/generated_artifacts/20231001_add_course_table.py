'''
Migration script to add Course table and relationship.
'''
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import text
# revision identifiers, used by Alembic.
revision = '20231001_add_course_table'  # Update with a unique revision ID
down_revision = None  # Update with the last migration revision ID if applicable
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
    # Create the student_courses association table
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer(), sa.ForeignKey('students.id'), primary_key=True),
        sa.Column('course_id', sa.Integer(), sa.ForeignKey('courses.id'), primary_key=True)
    )
def downgrade():
    op.drop_table('student_courses')
    op.drop_table('courses')