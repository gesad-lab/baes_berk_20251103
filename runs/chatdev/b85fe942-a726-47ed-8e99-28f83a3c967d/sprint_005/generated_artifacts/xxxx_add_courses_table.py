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
    # Note: Do not drop or alter existing tables to preserve data
def downgrade():
    # Drop the teachers table
    op.drop_table('teachers')
    # Drop the student_courses table
    op.drop_table('student_courses')
    # Drop the courses table
    op.drop_table('courses')