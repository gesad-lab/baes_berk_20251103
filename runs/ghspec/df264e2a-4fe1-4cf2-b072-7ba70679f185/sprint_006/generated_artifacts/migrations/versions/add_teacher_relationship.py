```python
"""Add Teacher relationship to Course

Revision ID: add_teacher_relationship
Revises: 
Create Date: 2023-10-12 12:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'add_teacher_relationship'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Add teacher_id column to courses table with foreign key constraint
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), sa.ForeignKey('teachers.id'), nullable=True))
    
    # Create the teachers table
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False)
    )


def downgrade():
    # Drop the teacher_id column from courses table
    op.drop_column('courses', 'teacher_id')
    
    # Drop the teachers table
    op.drop_table('teachers')
```