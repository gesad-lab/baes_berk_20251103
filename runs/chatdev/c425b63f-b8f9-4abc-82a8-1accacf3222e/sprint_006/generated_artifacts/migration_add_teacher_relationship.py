'''
Migration script to add teacher relationship to courses table.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = '20231001_04'  # Update with a new unique revision ID
down_revision = '20231001_03'  # Update with the previous migration revision ID
branch_labels = None
depends_on = None
def upgrade():
    '''
    Add teacher_id column to the courses table.
    '''
    op.add_column('courses', sa.Column('teacher_id', sa.Integer, sa.ForeignKey('teachers.id')))  # Ensure foreign key is added
def downgrade():
    '''
    Remove teacher_id column from the courses table.
    '''
    op.drop_column('courses', 'teacher_id')