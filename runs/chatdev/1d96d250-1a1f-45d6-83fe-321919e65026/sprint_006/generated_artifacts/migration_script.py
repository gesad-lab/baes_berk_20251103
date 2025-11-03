'''
Database migration script to add teachers table and teacher_id column to courses.
'''
from sqlalchemy import Column, String, Integer, ForeignKey
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'add_teachers_table'
down_revision = 'add_courses_table_and_association'
branch_labels = None
depends_on = None
def upgrade():
    '''
    Upgrade the database schema to add the teachers table and teacher_id column to courses.
    '''
    # Check if the teachers table already exists
    if not op.get_bind().has_table('teachers'):
        op.create_table(
            'teachers',
            sa.Column('id', sa.Integer(), nullable=False),
            sa.Column('name', sa.String(), nullable=False),
            sa.Column('email', sa.String(), nullable=False),
            sa.PrimaryKeyConstraint('id')
        )
    # Add teacher_id column to courses
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), sa.ForeignKey('teachers.id')))
def downgrade():
    '''
    Downgrade the database schema by removing the teachers table and teacher_id column from courses.
    '''
    op.drop_column('courses', 'teacher_id')
    op.drop_table('teachers')