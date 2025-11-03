'''
Migration script to add the teacher table.
'''
from alembic import op
import sqlalchemy as sa
def upgrade():
    # Create the teachers table
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False)
    )
    # Add the foreign key constraint for the existing courses table
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))
    op.create_foreign_key('fk_course_teacher', 'courses', 'teachers', ['teacher_id'], ['id'])
def downgrade():
    op.drop_constraint('fk_course_teacher', 'courses', type_='foreignkey')
    op.drop_column('courses', 'teacher_id')
    op.drop_table('teachers')