'''
Handles database migrations for the Student, Course, and Teacher entities.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'add_teacher_entity'
down_revision = 'add_course_relationship'
branch_labels = None
depends_on = None
def upgrade():
    '''Create teachers table and add teacher_id to courses table.'''
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False)
    )
    # Add teacher_id column as nullable first
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), sa.ForeignKey('teachers.id'), nullable=True))  
def downgrade():
    '''Drop teachers table and remove teacher_id from courses table.'''
    op.drop_column('courses', 'teacher_id')  # Remove teacher_id column
    op.drop_table('teachers')  # Drop teachers table