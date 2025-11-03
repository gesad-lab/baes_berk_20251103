from alembic import op
from sqlalchemy import Column, Integer, ForeignKey

# Upgrade function to add the teacher_id column to the courses table
def upgrade():
    # Adding the teacher_id column with a foreign key reference to the teachers table
    op.add_column('courses', Column('teacher_id', Integer, ForeignKey('teachers.id')))

# Downgrade function to remove the teacher_id column from the courses table
def downgrade():
    # Dropping the teacher_id column if it exists
    op.drop_column('courses', 'teacher_id')