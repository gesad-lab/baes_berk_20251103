'''
Migration script to add teacher_id column to Course entity.
'''
from alembic import op
import sqlalchemy as sa
def upgrade():
    '''
    Add teacher_id column to the courses table.
    '''
    op.add_column('courses', sa.Column('teacher_id', sa.Integer, sa.ForeignKey('teachers.id'), nullable=True))
def downgrade():
    '''
    Remove teacher_id column from the courses table.
    '''
    op.drop_column('courses', 'teacher_id')