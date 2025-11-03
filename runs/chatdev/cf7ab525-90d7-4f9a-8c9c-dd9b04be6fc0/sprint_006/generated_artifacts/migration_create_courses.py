'''
Migration script to create the courses table.
'''
from sqlalchemy import Column, Integer, String
from alembic import op
def upgrade():
    op.create_table(
        'courses',
        Column('id', Integer, primary_key=True, index=True),
        Column('name', String, nullable=False),
        Column('level', String, nullable=False),
        Column('teacher_id', Integer, ForeignKey('teachers.id'))  # Add this line
    )
def downgrade():
    op.drop_table('courses')