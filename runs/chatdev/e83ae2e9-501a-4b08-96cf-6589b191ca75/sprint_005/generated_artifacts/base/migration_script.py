'''
Migration script to add Course entity and ensure Student data is preserved.
'''
from alembic import op
import sqlalchemy as sa
def upgrade():
    '''
    Upgrade the database schema to include the courses table and the association table.
    '''
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False)
    )
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer(), sa.ForeignKey('students.id'), primary_key=True),
        sa.Column('course_id', sa.Integer(), sa.ForeignKey('courses.id'), primary_key=True)
    )
def downgrade():
    '''
    Downgrade the database schema by dropping the association table and the courses table.
    '''
    op.drop_table('student_courses')
    op.drop_table('courses')