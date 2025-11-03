'''
Database migration script to add courses table and student_courses association table.
'''
from sqlalchemy import Column, String, Integer, ForeignKey, Table
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'add_courses_table_and_association'
down_revision = 'add_email_column'
branch_labels = None
depends_on = None
def upgrade():
    '''
    Upgrade the database schema to add the courses table and association table.
    '''
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer(), nullable=False),
        sa.Column('course_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['student_id'], ['students.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['course_id'], ['courses.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('student_id', 'course_id')
    )
def downgrade():
    '''
    Downgrade the database schema by removing the courses table and association table.
    '''
    op.drop_table('student_courses')
    op.drop_table('courses')