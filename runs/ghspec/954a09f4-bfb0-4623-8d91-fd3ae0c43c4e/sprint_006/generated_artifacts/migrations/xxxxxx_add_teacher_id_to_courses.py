"""Add teacher_id column to courses table"""
from alembic import op
import sqlalchemy as sa

# Update the revision number as necessary
revision = 'xxxxxx'  
down_revision = 'previous_revision'  # Specify the previous migration's revision

def upgrade():
    # Add the 'teacher_id' column to the 'courses' table
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))
    
    # Create a foreign key constraint linking 'teacher_id' in 'courses' to 'id' in 'teachers'
    op.create_foreign_key('fk_teacher', 'courses', 'teachers', ['teacher_id'], ['id'])

def downgrade():
    # Remove the foreign key constraint and the 'teacher_id' column during a downgrade
    op.drop_constraint('fk_teacher', 'courses', type_='foreignkey')
    op.drop_column('courses', 'teacher_id')