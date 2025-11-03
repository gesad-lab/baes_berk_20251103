"""Add teacher relationship to courses

Revision ID: xxxx
Revises: previous_revision
Create Date: (create date)
"""

from alembic import op
import sqlalchemy as sa

revision = 'xxxx'
down_revision = 'previous_revision'

def upgrade() -> None:
    # Add teacher_id column to courses table, 
    # referencing the id field in the teachers table
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), sa.ForeignKey('teachers.id'), nullable=True))

def downgrade() -> None:
    # Remove teacher_id column from courses table
    op.drop_column('courses', 'teacher_id')